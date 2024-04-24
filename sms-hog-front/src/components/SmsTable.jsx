import {useQuery} from "@tanstack/react-query";
import axios from "axios";
import SETTINGS from "../settings";

function SmsTable() {
    const {isLoading, isError, data, error} =
        useQuery({
            queryKey: ["messages"],
            queryFn: async () => (await axios.get(SETTINGS.API_URL_GET_SMS)).data,
            refetchInterval: 1000
        });

    if (isLoading) {
        return <span aria-busy="true">Loading...</span>
    }

    if (isError) {
        return <span>Error: {error.message}</span>
    }

    return (
        <table>
            <thead>
            <tr>
                <th scope="col">Created At:</th>
                <th scope="col">Phone</th>
                <th scope="col">Message</th>
                <th scope="col">Headers</th>
            </tr>
            </thead>
            <tbody>
            {data?.data.sort(function (a, b) {
                let a_created_at = new Date(a.created_at);
                let b_created_at = new Date(b.created_at);
                return b_created_at - a_created_at;
            }).map((sms) => (
                <tr key={sms.id}>
                    <td>{(new Date(sms.created_at)).toLocaleString()}</td>
                    <td>{sms.phone}</td>
                    <td>{sms.message}</td>
                    <td>
                        <pre style={{margin: '0', lineHeight: '2em', padding: '0 0.5em'}}>{sms.headers.join('\n')}</pre>
                    </td>
                </tr>
            ))}
            </tbody>
        </table>
    )
}

export default SmsTable;
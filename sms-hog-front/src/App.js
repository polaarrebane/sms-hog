import React from 'react';
import './App.css';

import {
    QueryClient,
    QueryClientProvider,
} from '@tanstack/react-query'
import SmsTable from "./components/SmsTable";

const queryClient = new QueryClient()

function App() {
    return (
        <QueryClientProvider client={queryClient}>
            <SmsTable/>
        </QueryClientProvider>
    );
}

export default App;

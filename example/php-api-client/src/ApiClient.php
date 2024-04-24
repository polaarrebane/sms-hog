<?php

namespace ApiClient;

use GuzzleHttp\Client;

class ApiClient
{
    private Client $guzzleClient;

    public function __construct(
        string $baseUri,
    )
    {
        $this->guzzleClient = new Client([
            'base_uri' => $baseUri,
            'timeout' => 2.0,
        ]);
    }

    public function send(string $method, string $uri, array $headers, array $data): Response
    {
        try {
            $response = $this->guzzleClient->request(
                $method,
                $uri, [
                'headers' => $headers,
                'json' => $data,
            ]);
            $responseData = json_decode($response->getBody(), true, 512, JSON_THROW_ON_ERROR);
            return new Response($responseData);
        } catch (\Exception $e) {
            die($e->getMessage() . PHP_EOL);
        }
    }
}

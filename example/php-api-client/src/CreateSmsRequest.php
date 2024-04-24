<?php

namespace ApiClient;

class CreateSmsRequest
{
    private const METHOD = 'POST';

    private const URI = '/api/messages/sms';

    private ApiClient $apiClient;

    public function __construct(
        private readonly string $phone,
        private readonly string $message,
        private readonly array  $headers = [],
    )
    {
    }

    public function injectClient(ApiClient $apiClient): self
    {
        $this->apiClient = $apiClient;
        return $this;
    }

    public function send(): Response
    {
        return $this->apiClient->send(
            method: self::METHOD,
            uri: self::URI,
            headers: $this->headers,
            data: [
                'phone' => $this->phone,
                'message' => $this->message,
            ]
        );
    }
}

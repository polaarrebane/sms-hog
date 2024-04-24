<?php

namespace ApiClient;

class Response
{
    private array $data;

    public function __construct(...$data)
    {
        $this->data = $data;
    }

    public function toArray(): array
    {
        return $this->data;
    }
}

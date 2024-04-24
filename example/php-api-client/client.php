<?php

use Ramsey\Uuid\Uuid;

require __DIR__ . '/vendor/autoload.php';

$baseUri = getenv('API_URL_POST_SMS') ?: 'http://localhost:4000';
$client = new ApiClient\ApiClient($baseUri);
$message = $argv[1] ?? "SMS";
$phone = $argv[2] ?? "+79950000000";
$uuid = Uuid::uuid4()->toString();

$request = new \ApiClient\CreateSmsRequest(
    phone: $phone,
    message: $message,
    headers: [
        'x-request-id' => $uuid,
    ]
);

echo "request: " . PHP_EOL;
var_export([
    'phone' => $phone,
    'message' => $message,
    'headers' => [
        'x-request-id' => $uuid,
    ]
]);
echo PHP_EOL;

echo "response: " . PHP_EOL;
var_export($request->injectClient($client)->send()->toArray());
echo PHP_EOL;


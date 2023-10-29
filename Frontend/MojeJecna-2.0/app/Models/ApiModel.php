<?php
namespace App\Models;

use Nette\Http\Request;
class ApiModel
{
    private $apiUrl = 'https://api.example.com/';
    public function __construct(Client $httpClient)
    {
        $this->httpClient = $httpClient;
    }

    public function fetchData()
    {
        $response = $this->httpClient->get($this->apiUrl . 'endpoint');
        if ($response->isOk()) {
            return $response->getJson();
        } else {
            return null;  // Nebo vyvolání výjimky, podle potřeby
        }
    }

    public function login($username, $password)
    {
        $response = $this->httpClient->post($this->apiUrl . 'login', [
            'username' => $username,
            'password' => $password
        ]);
        if ($response->isOk()) {
            return $response->getJson();
        } else {
            return null;  // Nebo vyvolání výjimky, podle potřeby
        }
    }
}

# Exchange API Wrapper

This python project is to develop a wrapper for a cryptocurrency exchange's API to facilitate trading and data retrieval.

__Request Signature:__

 - The ```generate_signature``` method generates the request signature using HMAC-SHA256 encryption to ensure the authenticity and integrity of the request.

__Sending Requests:__

 - The ```send_request``` method sends a request to the exchange API, handles authentication by adding the API key and signature to the headers, and returns the response in JSON format.

__API Functions:__

 - The ```get_account_balance``` function retrieves the account balance from the exchange API.
 - The``` place_order``` function places an order on the exchange.
 - The ```get_order_status``` function retrieves the status of an order.


__Code Usage:__

 - Make sure you have the required libraries (requests, hashlib, hmac) installed before running the code. You can install them using the following command:
   
```bash
pip install requests
```
 - To use this code, replace the ```api_key```, ```secret_key```, and ```base_url``` variables with your actual API credentials and the base URL of the targeted cryptocurrency exchange's API.

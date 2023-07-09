import requests
import time
import hashlib
import hmac

class ExchangeAPIWrapper:
    def __init__(self, base_url, api_key, secret_key):
        self.base_url = base_url
        self.api_key = api_key
        self.secret_key = secret_key

    def generate_signature(self, payload):
        # Generate the request signature using HMAC-SHA256
        payload_string = "&".join([f"{key}={value}" for key, value in payload.items()])
        signature = hmac.new(self.secret_key.encode('utf-8'), payload_string.encode('utf-8'), hashlib.sha256).hexdigest()
        return signature

    def send_request(self, endpoint, method='GET', params=None):
        # Send a request to the exchange API
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': self.api_key
        }
        payload = {'timestamp': int(time.time())}
        if params:
            payload.update(params)
        payload['signature'] = self.generate_signature(payload)

        response = requests.request(method, url, headers=headers, params=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error sending request:", response.text)
            return None

    def get_account_balance(self):
        # Get account balance from the exchange API:
        endpoint = 'account/balance'
        response = self.send_request(endpoint)
        if response:
            return response['balance']
        else:
            return None

    def place_order(self, symbol, quantity, price, side):
        # Place an order on the exchange
        endpoint = 'order/place'
        params = {
            'symbol': symbol,
            'quantity': quantity,
            'price': price,
            'side': side
        }
        response = self.send_request(endpoint, method='POST', params=params)
        if response:
            return response['order_id']
        else:
            return None

    def get_order_status(self, order_id):
        # Get the status of an order
        endpoint = f'order/{order_id}'
        response = self.send_request(endpoint)
        if response:
            return response['status']
        else:
            return None

# Example usage:

# Define API credentials and base URL
api_key = "your_api_key"
secret_key = "your_secret_key"
base_url = "https://api.example.com"

# Create an instance of ExchangeAPIWrapper
exchange = ExchangeAPIWrapper(base_url, api_key, secret_key)

# Get account balance
balance = exchange.get_account_balance()
if balance:
    print("Account Balance:", balance)
else:
    print("Error retrieving account balance.")

# Place an order
symbol = "BTC/USD"
quantity = 0.1
price = 50000
side = "buy"
order_id = exchange.place_order(symbol, quantity, price, side)
if order_id:
    print("Order placed successfully. Order ID:", order_id)
else:
    print("Error placing order.")

# Get order status
if order_id:
    status = exchange.get_order_status(order_id)
    if status:
        print("Order Status:", status)
    else:
        print("Error retrieving order status.")

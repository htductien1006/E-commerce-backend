import requests


# Set up PayPal API credentials
client_id = "AbzJP11dcl8hYCiB3kRC0IraNFUs-srjlufAp0jRzYxcuHZgfOIA0QgJsuM9W6oLXvdZdEkzExuUnVbr"
secret = "ELVpZutgLucoDR1ZF23YuVezNx4Lds3spVTs7EufUtYjyQp1ixecu7Ka2xzs5EFVmu_YHsuvlrjIkmfV"
url = "https://api.sandbox.paypal.com"

# Set up API endpoints
base_url = url
token_url = base_url + '/v1/oauth2/token'
# payment_url = base_url + f'/v1/payments/payment/{paypal_id}/execute'
# print(payment_url)

# Request an access token
token_payload = {'grant_type': 'client_credentials'}
token_headers = {'Accept': 'application/json', 'Accept-Language': 'en_US'}
token_response = requests.post(token_url, auth=(client_id, secret), data=token_payload, headers=token_headers)

if token_response.status_code != 200:
    raise Exception('Failed to authenticate with PayPal API.')

access_token = token_response.json()['access_token']

# access_token = 'A21AAJXGtRpqGC2NvK2BnreMvUGrF87Yi3fdE9NjNoetXVhFjDZDbgCqxzqKRCVXDcVgCj7ObG3e398AEKmilyCTjoRUoRr8A'
print(access_token)
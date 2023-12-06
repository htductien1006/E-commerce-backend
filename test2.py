import requests
import json

access_token = 'A21AALm9WmgpwyUR5ZoHcJvZhqWXBXp01oy_Jj5VxcTVxdoi2thZzvEvQQN7gUuV0lO0zdFEPtsEzk1lLb5tsY6jL3YhYCdsA'

# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': f'Bearer {access_token}',
# }

# data = '{ "payer_id": "Q65Q3N8CPC2PC" }'

# response = requests.post(f'https://api-m.sandbox.paypal.com/v1/payments/payment/{paypal_id}/execute', headers=headers, data=data)

# print(response.status_code)
# if response == '<Response [200]>':
#     print("Payment success")

    # access_token = token_response.json()['access_token']
print(access_token)


paypal_id = 'PAYID-MVYJ7FQ3DU79597GF4541222'
# Retrieve payment details
payment_headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}'
}

payment_url = f'https://api-m.sandbox.paypal.com/v1/payments/payment'

payer_id = "Q65Q3N8CPC2PC"

payment_details_url = f'{payment_url}/{paypal_id}/execute'
data = { "payer_id": f'{payer_id}' }
payment_details_response = requests.post(payment_details_url, data=json.dumps(data) ,headers=payment_headers)

print(payment_details_response.status_code)

if payment_details_response.status_code != 200:
    raise Exception('Failed to retrieve PayPal payment details.')

else:
    print("Done")
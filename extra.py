import requests
import json

url = "http://127.0.0.1:8000/api/invoices/"

payload = json.dumps({
  "cash_in_bank": -14.61,
  "total_current_assets": -14.61,
  "total_assets": -14.61,
  "net_income": 0,
  "opening_balance_equity": -23.45,
  "owner_loan": 576,
  "retained_earnings": -567.16
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

import requests

response = requests.get("http://127.0.0.1:5000/get_user_settings?telegram_id=123456789")
if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code)

import requests

url = "http://127.0.0.1:5000/update_user_settings"
data = {
    "telegram_id": "123456789",
    "settings": {
        "min_purchase": 15.0,
        "min_liquidity": 1500.0,
        "max_liquidity": 5500.0,
        "min_token_holders": 150,
        "max_buy_tax": 4.5,
        "max_sell_tax": 4.5,
        "min_slippage": 0.4,
        "min_price_impact": 0.9,
        "bribe": 45.0,
        "max_purchase": 1500.0
    }
}

response = requests.post(url, json=data)
print(response.json())

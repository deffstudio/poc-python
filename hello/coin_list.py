import requests

url = "https://api.coingecko.com/api/v3/coins/list"

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": "CG-uZXYz242wkTg5qWMihjbLLqu"
}

response = requests.get(url, headers=headers)

print(response.text)
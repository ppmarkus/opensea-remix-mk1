from urllib import response
import requests

url: str = "https://api.opensea.io/api/v1/assets?order_by=pk&order_direction=desc&limit=20&include_orders=true"

headers: dict = {"Accept": "application/json"}

r: response = requests.request("GET", url, headers=headers)

print(r.status_code)
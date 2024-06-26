import requests

url = "https://e354-35-240-129-156.ngrok-free.app/query"
payload = {"query": "풋살에 대해서 알려줘"}
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=payload, headers=headers)
print(response.json())

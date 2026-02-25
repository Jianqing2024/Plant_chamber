import requests

url = "http://8.134.80.214:8080/upload"

data = {
    "device_id": "chamber1",
    "temperature": 25.5,
    "humidity": 60
}

r = requests.post(url, json=data)

print(r.status_code)
print(r.text)
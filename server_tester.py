import requests as requests

data = {
    "engine_temperature": 1.2,
}

response = requests.post("http://0.0.0.0:8000/record", json=data)
print(response.content)

response = requests.post("http://0.0.0.0:8000/collect")
print(response.content)

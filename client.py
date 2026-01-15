import requests

url = "http://127.0.0.1:5000/check"

payload = {
    "message" : "is it working?"
}

response = requests.post(url,json=payload)

print("status code:" , response.status_code)
print("response json:" , response.json())
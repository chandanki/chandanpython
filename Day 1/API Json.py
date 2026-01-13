import requests

url = 'https://petstore.swagger.io/v2/swagger.json'
response = requests.get(url)
if response.status_code == 200:
    print('data:',response.json())
else:
    print("data not found")

# for Post request
url = ""
headers = {}
data = {}
response = requests.post(url,json=data, headers=headers)
if response.status_code == 201:
    print('data found', response.json())
else:
    print("data Not found")

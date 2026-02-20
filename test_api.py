import requests

response = requests.get('http://localhost:5000/')
print(f"Status Code: {response.status_code}")
print(f"Content: {response.text}")

response = requests.get('http://localhost:5000/about')
print(response.json())

response = requests.get('http://localhost:5000/greet/John')
print(response.text)

response = requests.get('http://localhost:5000/calculate?num1=10&num2=5&operation=add')
print(response.text)

response = requests.get('http://localhost:5000/calculate?num1=10&num2=0&operation=divide')
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

response = requests.post(
    'http://localhost:5000/echo',
    json={"message": "Hello Flask"}
)
print(response.json())

response_200 = requests.get('http://localhost:5000/status/200')
response_404 = requests.get('http://localhost:5000/status/404')
print(response_200.status_code, response_200.text)
print(response_404.status_code, response_404.text)

response = requests.get('http://localhost:5000/')
custom_header = response.headers.get('X-Custom-Header')
print(f"Custom Header: {custom_header}")
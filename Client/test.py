import requests

url = "https://httpbin.org/get"

# 发送GET请求
response = requests.get(url)

# 打印返回内容
print("状态码:", response.status_code)
print("响应内容:")
print(response.text)
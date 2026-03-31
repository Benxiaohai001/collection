import requests, json

# url = "http://127.0.0.1:8901/metrics"
url = "http://127.0.0.1:8901/debug"
response = requests.get(url)

# 打印 HTTP 状态码
print(f"Status Code: {response.status_code}")

# # 打印响应头
# print(f"Headers: {response.headers}")

# # 打印响应内容（字符串形式）
# print(f"Text: {response.text}")
print(f"Type: {type(response.text)}")
count = 1
for i in response.text.split("\n"):
    print(count)
    print(i)
    count += 1

# 打印响应内容（JSON 形式）
# json_data = json.loads(response.text)
# print(f"JSON Data: {json_data}")
# try:
#     json_data = response.json()
#     print(f"JSON Data: {json_data}")
# except ValueError:
#     print("Response content is not in JSON format")

# # 打印最终请求的 URL
# print(f"URL: {response.url}")

# # 打印响应时间
# print(f"Elapsed Time: {response.elapsed}")

# # 打印 cookies
# print(f"Cookies: {response.cookies}")
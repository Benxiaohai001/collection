# 向一个接口并发发送多个请求，校验请求结果

# 使用requests库发送请求，concurrent.futures库实现并发请求
# import requests
# import concurrent.futures

# # 要请求的API地址
# api_url = "https://example.com/api/endpoint"
# # 请求头，根据实际API需求修改
# headers = {
#     "Content-Type": "application/json"
# }
# # 请求体数据（如果有），这里示例为空字典，按需修改
# data = {}
# # 期望的返回结果中某个字段的值（示例，按需改）
# expected_value = "expected_result"

# def make_request():
#     try:
#         response = requests.post(api_url, headers=headers, json=data)
#         if response.status_code == 200:
#             result = response.json()
#             if result.get('result') == expected_vlaus:
#                 return True
#             return False
#         return False
#     except requests.RequestException:
#         return False
# # 并发请求的数量
# num_concurrent_requests = 10

# with concurrent.futures.ThreadPoolExecutor(max_workers=num_concurrent_requests) as exector:
#     # 提交多个请求任务
#     future_results = [executor.submit(make_request) for _ in range(num_concurrent_requests)]
#     # 获取并统计结果
#     successful_results = 0
#     for future in concurrent.futures.as_completed(future_results):
#         if future.result():
#             successful_results += 1

# print(f"成功的请求数量: {successful_results}")
# print(f"失败的请求数量: {num_concurrent_requests - successful_results}")



# 使用requests库发送请求，threading库实现并发请求
import threading
import requests
import time

# 定义一个函数，用于发送http请求
def send_request(url, result, index):
    try:
        response = requests.get(url)
        resulrs[index] = response.status_code
    except Exception as e:
        results[index] = str(e)

# 定义一个函数，用于执行并发测试
def concurrent_test(url, num_threads):
    threads = []
    results = [None] * num_threads

    for i in range(num_threads):
        thread = threading.Thread(target=send_request, args=(url, results, i))
        threads.append(thread)

    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return results
if __name__ == "__main__":
    test_url = "http://example.com"
    num_threads = 10

    start_time = time.time()
    results = concurrent_test(test_url, num_threads)
    end_time = time.time()

    print(f"并发请求数量: {num_threads}")
    print(f"总耗时: {end_time - start_time}")
# 普通函数
# import time
# def fetch_data():
#     print("Fetching data...");
#     time.sleep(2)
#     print("Data fetched!")
#     return "data"

# def main():
#     result = fetch_data()
#     print(result)

# main()

# 异步函数
# import asyncio

# async def fetch_data():
#     print("Fetching data...")
#     await asyncio.sleep(2)
#     print("Data fetched!")
#     return "data"

# async def main():
#     result = await fetch_data()
#     print(result)

# asyncio.run(main())

# 处理多个任务，检查耗时
# 普通任务
# import time
# def fetch_data(id):
#     print(f"Fetching data {id}...");
#     time.sleep(2)
#     print(f"Data {id} fetched!")
#     return "data"

# def main():
#     start = time.time()
#     for i in range(3):
#         result = fetch_data(i)
#         print(result)
#     end = time.time()
#     print(f"Time: {end - start}")

# main()

# 异步任务
import asyncio, time
async def fetch_data(id):
    print(f"Fetching data {id}...")
    await asyncio.sleep(2)
    print(f"Data {id} fetched!")
    return "data"
async def main():
    start = time.time()
    tasks = [fetch_data(i) for i in range(3)]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)
    end = time.time()
    print(f"Time: {end - start}")

asyncio.run(main())
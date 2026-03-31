def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter
# 创建计数器实例
counter1 = make_counter()
counter2 = make_counter()

# 调用计数器
print(counter1())  # 输出: 1
print(counter1())  # 输出: 2
print(counter2())  # 输出: 1
print(counter2())  # 输出: 2
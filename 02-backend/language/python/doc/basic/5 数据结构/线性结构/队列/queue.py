# from collections import deque
# import itertools
# # 保留最后n个元素, 类似于linux的tail命令
# # 函数会加载文家中所有行的值，但是容量只有n，后进先出，所以最后保留的值只有最后n个值
# def tail(filename, n=10):
#     with open(filename) as f:
#         return deque(f, n)

# # 维护一个近期添加的元素序列
# # 保留最后n个元素
# def moving_average(iterable, n=3):
#     it = iter(iterable)
#     d = deque(itertools.islice(it, n-1))
#     d.appendleft(0)
#     s = sum(d)
#     for elem in it:
#         s += elem - d.popleft()
#         print(f"elem: {elem}, s: {s}, d: {d}")
#         d.append(elem)
#         print(f"d: {d}")
#         # yield s / n


# if __name__ == '__main__':
#     # print(tail('queue.txt'))
#     # print(moving_average([40, 30, 50, 46, 39, 44]))
#     m = moving_average([40, 30, 50, 46, 39, 44])
#     # for  i in m:
#     #     print(i)


# 自己实现一个队列
# FIFO
# 用列表实现队列
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
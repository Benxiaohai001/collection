# 容器数据类型
## ChainMap对象
## deque 对象
```python3
>>> from collections import deque
>>> d = deque('ghi')
```
* append(x)
添加到右端
```python3
>>> d.append('c')
>>> d
deque(['g', 'h', 'i', 'c'])
```
* appendleft(x)
添加到左端
```python3
>>> d.appendleft('d')
>>> d
deque(['d', 'g', 'h', 'i', 'c'])
```
* clear()
移除所有元素
* copy()
创建一份浅拷贝
```python3
>>> d1 = d.copy()
>>> d1
deque(['d', 'g', 'h', 'i', 'c'])
```
* count(x)
计算x的个数
```python3
>>> d1.count('i')
1
```
* extend(iterable)
扩展右侧
```python3
>>> d.extend(d1)
>>> d.extend(d1) 
>>> d
deque(['d', 'g', 'h', 'i', 'c', 'd', 'g', 'h', 'i', 'c'])
>>> d1
deque(['d', 'g', 'h', 'i', 'c'])
```
* extendleft(iterable)
扩展左侧
```python3
* index(x[,start[,end]])
# 返回第一个x的索引，不存在报错
>>> d1.index('h')
2
>>> d1.index('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'a' is not in deque

# insert(i, x)
# 向i插入x
>>> d1.insert(1, 'a')
>>> d1
deque(['d', 'a', 'g', 'h', 'i', 'c', 'd', 'g', 'h', 'i', 'c'])
# pop()
# 返回最后一个
>>> d1
deque(['d', 'a', 'g', 'h', 'i', 'c', 'd', 'g', 'h', 'i', 'c'])
>>> d1.pop()
'c'
>>> d1
deque(['d', 'a', 'g', 'h', 'i', 'c', 'd', 'g', 'h', 'i'])
# popleft()
# 返回最左边的元素
>>> d1
deque(['d', 'a', 'g', 'h', 'i', 'c', 'd', 'g', 'h', 'i'])
>>> d1.popleft()
'd'
>>> d1
deque(['a', 'g', 'h', 'i', 'c', 'd', 'g', 'h', 'i'])
# remove(value)
# 移出第一个value
>>> d1
deque(['a', 'g', 'h', 'i', 'c', 'd', 'g', 'h', 'i'])
>>> d1.remove('g')
>>> d1
deque(['a', 'h', 'i', 'c', 'd', 'g', 'h', 'i'])
# reverse()
# 排序
>>> d1
deque(['i', 'h', 'g', 'd', 'c', 'i', 'h', 'a'])
>>> d1.reverse()
>>> d1
deque(['a', 'h', 'i', 'c', 'd', 'g', 'h', 'i'])
# rotate(n=1)
向右移动
>>> d1
deque(['a', 'h', 'i', 'c', 'd', 'g', 'h', 'i'])
>>> d1.rotate(n=2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: deque.rotate() takes no keyword arguments
>>> d1.rotate(2)  
>>> d1
deque(['h', 'i', 'a', 'h', 'i', 'c', 'd', 'g'])
>>> d1.rotate(-2) 
>>> d1
deque(['a', 'h', 'i', 'c', 'd', 'g', 'h', 'i'])
maxlen
返回最大尺寸，没有返回None
>>> d1.maxlen  
>>> print(d1.maxlen)
None
```

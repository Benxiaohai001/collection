# Data Structure
## fundamental Data Structure
## Custom Data Structures
# 排序
## 数据分析
组织和分析一个大的数据集
## 用户接口
以一定的顺序展示，像文件按照名称、大小、时间
## 数据系统
按顺序尽快的查找
## 算法设计
一些算法依赖于对输入数据进行排序。

## 冒泡排序
```python3
def bubble_sort(lst):

    # outer loop to access each list element
    for i in range(len(lst)):

        # inner loop to compare list elements
        for j in range(len(lst) - 1):

            # swap elements if necessary
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst       

data_list = [15, 16, 6, 8, 5]
print(f"Unsorted List: {data_list}")

sorted_list = bubble_sort(data_list)

print(f"Sorted List: {sorted_list}")
```
自己写的;严格来说不是冒泡排序，选择排序
```python3
def bubble_sort(lst):

    # outer loop to access each list element
    for i in range(len(lst)):

        # inner loop to compare list elements
        for j in range(i, len(lst)):

            # swap elements if necessary
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst       

# data_list = [15, 16, 6, 8, 5]
data_list = [3, 2, 1]
print(f"Unsorted List: {data_list}")

sorted_list = bubble_sort(data_list)

print(f"Sorted List: {sorted_list}")
```
倒序
```python3
def bubble_sort_desc(lst):
    # write your code here
    for i in range(len(lst)):
        
        for j in range(len(lst) - 1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            print(f"j: {j}, lst: {lst}")  
        print(f"i: {i}, lst: {lst}")
    return lst
```
### 优化
```python3
# Bubble sort in ascending order
def bubble_sort(data):
    # 当倒数第二个最大值找到的情况下，倒数第一个也是确定的，不用再次循环
    for i in range(len(data) - 1):
        swapped = False
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        # 如果在一轮遍历中没有发生数据转换，则证明数据是有序的，直接中止循环。
        if not swapped: 
            break
        
    return data
 
data_list = [4, 6, 99, 45, 0]
 
sorted_list = bubble_sort(data_list)
print(sorted_list)
```
### 支持的场景
* 少量数据集
* 简单比效率更重要时
* 数据早已部分排序
### 不支持的场景
* 大规模的数据集，且更在意效率的应用
* 在这种场景下需要考虑使用归并排序和快速排序
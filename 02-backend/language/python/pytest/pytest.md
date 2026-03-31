# post上传文件
post上传文件时，不要指定headers中content-type
# 参数序列化
@pytest.mark.parametrize # fixture
```python3
import pytest

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (4, 5, 9), ( - 1, 1, 0)])
def test_add_numbers(a, b, expected):
    result = add_numbers(a, b)
    assert result == expected

@pytest.mark.parametrize("p1, p2, expected", [
    (Point(0, 0), Point(3, 4), 5),
    (Point(1, 1), Point(1, 1), 0)
])
def test_distance(p1, p2, expected):
    result = distance(p1, p2)
    assert result == expected

import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]

@pytest.mark.parametrize("data_item", [0, 1, 2])
def test_with_fixture(sample_data, data_item):
    assert sample_data[data_item] in sample_data
```
## 使用yaml进行序列化
假设我们测试如下函数：
```python3
       def add_numbers(a, b):
           return a + b
```
使用yaml进行序列化
1. `pip install pyyaml` # 安装依赖包
2. 创建yaml文件
```yaml
# test_data.yaml
add_tests:
  - a: 1
    b: 2
    expected: 3
  - a: 10
    b: 20
    expected: 30
  - a: -1
    b: 1
    expected: 0
```
3. 编写测例
```python3
import pytest
import yaml

# 被测试函数
def add_numbers(a, b):
    return a + b

# 从 yaml 文件中读取测试数据
def load_test_data(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# 加载测试数据
test_data = load_test_data('test_data.yaml')['add_tests']

# 参数化测试
@pytest.mark.parametrize("test_case", test_data)
def test_add_numbers(test_case):
    a = test_case['a']
    b = test_case['b']
    expected = test_case['expected']
    assert add_numbers(a, b) == expected
```
## 使用json文件
1. 编写json测试数据
```json
{
    "add_tests": [
        {"a": 1, "b": 2, "expected": 3},
        {"a": 10, "b": 20, "expected": 30},
        {"a": -1, "b": 1, "expected": 0}
    ]
}
```
2. 测例
```python
import pytest
import json

# 被测试函数
def add_numbers(a, b):
    return a + b

# 从 JSON 文件中读取测试数据
def load_test_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# 加载测试数据
test_data = load_test_data('test_data.json')['add_tests']

# 参数化测试
@pytest.mark.parametrize("test_case", test_data)
def test_add_numbers(test_case):
    a = test_case['a']
    b = test_case['b']
    expected = test_case['expected']
    assert add_numbers(a, b) == expected
```
## csv文件进行序列化
1. csv文件
```csv
a,b,expected
1,2,3
10,20,30
-1,1,0
```
2. 测例
```python3
import pytest
import csv

# 被测函数
def add_number(a, b):
    return a + b

# 从csv文件中读取测试数据
def load_test_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

# 加载测试数据
test_data = load_test_data('test_data.csv')

# 参数化测试
@pytest.mark.parametrize("test_case", test_data)
def test_add_number(test_case):
    a = int(test_case['a'])
    b = int(test_case['b'])
    expected = int(test_case['expected'])
    assert add_number(a, b) == expected
```

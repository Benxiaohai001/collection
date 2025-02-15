# [参考](https://zhuanlan.zhihu.com/p/23343991437)
# 理解关键
* @decorator 等价于 func = decorator(func)
* 保证目标函数在不改变的条件下，利用装饰器进行若干功能的模块化拓展
* 装饰器可一次定义出多个应用，并按照目标函数处的堆叠顺序，自下而上执行
```python
def syrup_decorator(coffee_maker):
    def add_syrup():
        coffee = coffee_maker()
        return coffee + " + 特质糖浆"
    return add_syrup

def cream_decorator(coffee_maker):
    def add_cream():
        coffee = coffee_maker()
        return coffee + "+ 特质奶油"
    return add_cream

@syrup_decorator
@cream_decorator
def make_coffee():
    return "咖啡"

print(make_coffee())  # 咖啡 + 特质奶油 + 特质糖浆
```
# 2. 参数化函数装饰器
```python
def flavored_syrup(syrup_type):
    # 口味配置字典
    flavor_map = {
        "vanilla": "+ 香草糖浆",
        "hazelnut": "+ 榛果糖浆",
    }
    def syrup_decorator(coffee_maker):
        def add_syrup():
            coffee = coffee_maker()
            return coffee + flavor_map[syrup_type]
        return add_syrup
    return syrup_decorator

# 奶油装饰器
def quantity_cream(cream_type):
    # 分量配置
    quant_map = {
        "light": "+ light",
        "normal": "+ normal",
        "extra": "+ extra",
    }
    def cream_decorator(coffee_maker):
        def add_cream():
            coffee = coffee_maker()
            return coffee + quant_map[cream_type]
        return add_cream
    return cream_decorator

# 支持温度控制进阶装饰器
def temperature_control(ice=False):
    def decorator(coffee_maker):
        def wrapper():
            coffee = coffee_maker()
            return f"{coffee}" if ice else f" ice {coffee}"
        return wrapper
    return decorator

# 点单制作咖啡的目标函数
def order_coffee():
    return " coffee "

# 顾客a的订单
@quantity_cream("extra")
@flavored_syrup("hazelnut")
@temperature_control()
def customer_a():
    return order_coffee()

# 顾客b的订单
@quantity_cream("normal")
@flavored_syrup("vanilla")
@temperature_control(True)
def customer_b():
    return order_coffee()

print(customer_a(), customer_b(), sep="\n")
# 输出
# ice  coffee + 榛果糖浆+ extra
#  coffee + 香草糖浆+ normal
```
## 理解关键
* 相比于无参数的双层嵌套结构，含参数的具有三层嵌套的结构，优先处理配置参数，再处理目标函数
* @decorator(param)等价于func = decorator(func(param))
* 经典的场景包括：web框架路由配置（@app.route('/path')）、权限分级控制(@admin_required(level=3))、重试机制配置（@retry(time=3, delay=2)）、缓存设置(@cache(expire=300))、输入参数验证(@validate_type(int))、日志级别控制(@log_level('DEBUG'))等
# 3. 无参数类装饰器
```python
class SyrupDecorator:
    def __init__(self, func):
        self.syrup_func = func
        self.__name__ = func.__name__
    
    def __call__(self):
        print(f" start syrup (decorator {self.syrup_func.__name__})")
        coffee = self.syrup_func()
        return coffee + " + syrup"

# 类形式奶油装饰器
class CreamDecorator:
    def __init__(self, func):
        self.cream_func = func
        self.__name__ = func.__name__

    def __call__(self):
        print(f" start cream (decorator {self.cream_func.__name__})")
        coffee = self.cream_func()
        return coffee + " + cream"

# 类形式制作计数器
class CoffeeLogger:
    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__
        self.count = 0

    def __call__(self):
        self.count += 1
        print(f" start make coffee {self.count} times")
        result = self.func()
        print(f" end make {self.count} coffee, {result}\n")

# 点单制作咖啡的目标函数
@CoffeeLogger
@CreamDecorator
@SyrupDecorator
def order_coffee():
    return " coffee "


for _ in ['customer_a', 'customer_b']:
    order_coffee()
```
## 关键
1. 0



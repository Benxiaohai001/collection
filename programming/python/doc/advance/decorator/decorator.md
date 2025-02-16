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
1. 目标函数属性（例如，func.__name__）可以通过实例属性存储，而不依赖闭包捕获，从而关丽丽需要维持状态复杂装饰逻辑。
2. 像现实中的自动咖啡机，既能保持核心咖啡萃取功能不变，又能通过模块化的硬件组件（类方法）实现更稳定、可扩展的风味增强系统
# 4. 参数化类装饰器
```python
class FlavoredSyrup:
    def __init__(self, syrup_type):
        self.flavor_map = {
            "vanilla": " + vanilla syrup",
            "hazelnut": " + hazelnut syrup",
        }
        self.flavor = self.flavor_map[syrup_type]

    def __call__(self, func):
        class TempDecorator:
            def __init__(self, targ_func, flavor):
                self.syrup_func = targ_func
                self.__name__ = func.__name__
                self.flavor = flavor
            def __call__(self):
                print(f" start syrup (decorator {self.syrup_func.__name__} function)")
                return self.syrup_func() + self.flavor
        return TempDecorator(func, self.flavor)


# 奶油参数化类装饰器
class QuantityCream:
    def __init__(self, cream_type):
        self.quant_map = {
            "normal": " + normal cream",
            "double": " + double cream",
        }      
        self.quant = self.quant_map[cream_type]

    def __call__(self, func):
        class TempDecorator:
            def __init__(self, targ_func, quant):
                self.cream_func = targ_func
                self.__name__ = func.__name__
                self.quant = quant
            
            def __call__(self):
                print(f" start cream (decorator {self.__name__} function)")
                return self.cream_func() + self.quant
        return TempDecorator(func, self.quant)

# 温度参数化类装饰器
class TemperatureControl:
    def __init__(self, ice=False):
        self.ice = ice

    def __call__(self, func):
        class TempDecorator:
            def __init__(self, targ_func, ice):
                self.func = targ_func
                self.__name__ = targ_func.__name__
                self.ice = ice

            def __call__(self):
                return f" {self.func()}" if self.ice else f" ice {self.func()}"
        
        return TempDecorator(func, self.ice)

# 点单制作咖啡的目标函数
def order_coffee():
    return " coffee "

# 顾客a的订单
@QuantityCream("double")
@FlavoredSyrup("hazelnut")
@TemperatureControl(False)
def customer_a():
    return order_coffee()

# 顾客b的订单
@QuantityCream("normal")
@FlavoredSyrup("vanilla")
@TemperatureControl(True)
def customer_b():
    return order_coffee()


print(customer_a(), customer_b(), sep="\n")
```
## 理解
1. 与进阶手背装饰函数的基础类装饰器相比，参数化类装饰器可以实现接受配置参数，再接受函数；
2. 参数化类装饰器的代码为嵌套包装类设计，支持多配置实例复杂逻辑；
3. 工业级场景包括：设备参数预设（温度、压力、剂量）、服务限流控制（最大调用次数）、版本兼容处理（API版本路由）、多环境配置（开发、测试、生产）、动态权限管理（角色访问控制）、A/B系统测试（实验分组配置）等



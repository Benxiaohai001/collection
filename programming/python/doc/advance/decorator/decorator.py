# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
# @my_decorator
# def say_whee():
#     print("Whee!")
# say_whee()

# 参考： https://zhuanlan.zhihu.com/p/23343991437
# def syrup_decorator(coffee_maker):
#     def add_syrup():
#         coffee = coffee_maker()
#         return coffee + " + 特质糖浆"
#     return add_syrup

# def cream_decorator(coffee_maker):
#     def add_cream():
#         coffee = coffee_maker()
#         return coffee + "+ 特质奶油"
#     return add_cream

# @syrup_decorator
# @cream_decorator
# def make_coffee():
#     return "咖啡"

# print(make_coffee())  # 咖啡 + 特质奶油 + 特质糖浆
# 这里有一点，装饰器的执行顺序是从下往上的，所以先执行cream_decorator，再执行syrup_decorator

# 2. 装饰器的参数
# 糖浆装饰器
# def flavored_syrup(syrup_type):
#     # 口味配置字典
#     flavor_map = {
#         "vanilla": "+ 香草糖浆",
#         "hazelnut": "+ 榛果糖浆",
#     }
#     def syrup_decorator(coffee_maker):
#         def add_syrup():
#             coffee = coffee_maker()
#             return coffee + flavor_map[syrup_type]
#         return add_syrup
#     return syrup_decorator

# # 奶油装饰器
# def quantity_cream(cream_type):
#     # 分量配置
#     quant_map = {
#         "light": "+ light",
#         "normal": "+ normal",
#         "extra": "+ extra",
#     }
#     def cream_decorator(coffee_maker):
#         def add_cream():
#             coffee = coffee_maker()
#             return coffee + quant_map[cream_type]
#         return add_cream
#     return cream_decorator

# # 支持温度控制进阶装饰器
# def temperature_control(ice=False):
#     def decorator(coffee_maker):
#         def wrapper():
#             coffee = coffee_maker()
#             return f"{coffee}" if ice else f" ice {coffee}"
#         return wrapper
#     return decorator

# # 点单制作咖啡的目标函数
# def order_coffee():
#     return " coffee "

# # 顾客a的订单
# @quantity_cream("extra")
# @flavored_syrup("hazelnut")
# @temperature_control()
# def customer_a():
#     return order_coffee()

# # 顾客b的订单
# @quantity_cream("normal")
# @flavored_syrup("vanilla")
# @temperature_control(True)
# def customer_b():
#     return order_coffee()

# print(customer_a(), customer_b(), sep="\n")

# 3 无参数的类装饰器
# 类形式糖浆装饰器
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
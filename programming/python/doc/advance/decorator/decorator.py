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
# class SyrupDecorator:
#     def __init__(self, func):
#         self.syrup_func = func
#         self.__name__ = func.__name__
    
#     def __call__(self):
#         print(f" start syrup (decorator {self.syrup_func.__name__})")
#         coffee = self.syrup_func()
#         return coffee + " + syrup"

# # 类形式奶油装饰器
# class CreamDecorator:
#     def __init__(self, func):
#         self.cream_func = func
#         self.__name__ = func.__name__

#     def __call__(self):
#         print(f" start cream (decorator {self.cream_func.__name__})")
#         coffee = self.cream_func()
#         return coffee + " + cream"

# # 类形式制作计数器
# class CoffeeLogger:
#     def __init__(self, func):
#         self.func = func
#         self.__name__ = func.__name__
#         self.count = 0

#     def __call__(self):
#         self.count += 1
#         print(f" start make coffee {self.count} times")
#         result = self.func()
#         print(f" end make {self.count} coffee, {result}\n")

# # 点单制作咖啡的目标函数
# @CoffeeLogger
# @CreamDecorator
# @SyrupDecorator
# def order_coffee():
#     return " coffee "


# for _ in ['customer_a', 'customer_b']:
#     order_coffee()

# # 输出结果
# '''
#  start make coffee 1 times
#  start cream (decorator order_coffee)
#  start syrup (decorator order_coffee)
#  end make 1 coffee,  coffee  + syrup + cream

#  start make coffee 2 times
#  start cream (decorator order_coffee)
#  start syrup (decorator order_coffee)
#  end make 2 coffee,  coffee  + syrup + cream
#  '''
#  # 这里有一点，为什么没有对实例进行引用，但是缺调用了__call__方法？
# '''
# 在 Python 中，装饰器是一种特殊的函数或类，它们可以在不修改原始函数代码的情况下，扩展或修改函数的行为。当你使用类作为装饰器时，类的 __call__ 方法会被调用。
# 在你的代码中，CoffeeLogger、CreamDecorator 和 SyrupDecorator 可能是类装饰器。类装饰器需要实现 __call__ 方法，这样当装饰的函数被调用时，__call__ 方法就会被执行。
# '''

# 4. 有参数的类装饰器
# 糖浆参数化类装饰器
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
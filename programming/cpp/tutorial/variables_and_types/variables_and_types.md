# 变量和类型

# 标识符
字符，数字，_
字符，_ 开头
不能和关键字重名，不能和额外的关键字重名
大小写敏感
# 基础数据类型
## 字符类型
    char 一个字节 
    char16_t 至少两个字节
    char32_t 至少四个字节；
    wchar_t 最大数量的字符集
## 整型
    有符号的
    无符号的
## 浮点类型
## 布尔值
## void
## 空指针
# 变量声明
强类型语言

# 初始化变量
c语言式初始化
int x = 0；
构造器式初始化
int x(0);
统一的初始化；列表初始化；
int x {0}
# 类型推断：自动声明类型
int foo = 0;
auto bar = foo; // the same as : int bar = foo;

int foo =0;
decltype(foo) bar; // the same as : int bar;

# 字符串介绍
# constants
固定的值
# 字面值
75 // 十进制
0113 // 八进制
0x4b // 16进制
## 单精度和双精度浮点数区别：
### 单精度
7位小数
4个字节
占用空间少，性能高（现在计算机这里的性能差基本可以忽略）
### 双精度
15-16位小数
8个字节
范围大，精度高

### 字符和字符串常量
有引号（"",''） 用于区分变量名和关键字
'':字符
“”：字符串
### 特殊字符
\n 新行
\r 回车
\t tab
\v 垂直tab
\b 退格键
\f 种子
\a 
\'
\"
\? 
\\
\ 续行符
### ASCII
使用前缀代表字符类型 大小写敏感
u char16_t
U char32_t
L wchar_t
对于字符串
u8 utf-8
R 原始字符串
### 其他字面量
true, false, nullptr
## 类型化常量表达式
const double pi =3.1415926;
const char tab = '\t';
## 预处理定义
```
#define identifier replacement
```
预处理是在编译之前， 后续的identifier 会与replacement 进行绑定
后面不需要分号;如果后续出现分号，可能会报错；
单独存在一行；

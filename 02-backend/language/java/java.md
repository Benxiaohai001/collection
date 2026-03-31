_JAVA_OPTIONS="--add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED"

_JAVA_OPTIONS: ORACLE JVM 定义的，通过配置操作系统环境变量设置
# 文件
java 源码文件
class 字节码文件
# 关键字
* final 修饰类，方法和变量 \
变量：修饰之后表示该变量只能负值一次，不可修改
# 概念
## 多态
* 方法重载： 同一个类中定义同名的多个方法，他们接受的参数不同。调用方法时根据参数类型区分不同的方法；
## 构造器
特殊的方法，用于创建对象并初始化对象成员变量。每个类至少有一个构造器，构造器可以重载；
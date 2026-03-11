[line protocol](https://docs.influxdata.com/influxdb/v1/write_protocols/line_protocol_tutorial/)主要有组件的数据类型：表名，标签键，标签值，字段键，字段值和时间戳。
# 时间戳 
最小有效时间-9223372036854775806或1677-09-21T00:12:43.145224194Z。最大时间戳为9223372036854775806或2262-04-11T23:47:16.854775806Z。默认情况下，时间戳的精度是纳秒。
# 字段值
字段值可以是浮点数、整数、字符串或布尔值：
* 浮点数
默认情况下，假定所有的值都是浮点数；如下82为浮点数
```
weather,location=us-midwest temperature=82 1465839830100400200
```
* 整数 
将一个“i”到字段值以告诉 db 将该数字存储为整数。
将字段值存储82为整数：
```
weather,location=us-midwest temperature=82i 1465839830100400200
```
* 字符串
双引号字符串字段值
将字段值存储too warm为字符串：
```
weather,location=us-midwest temperature="too warm" 1465839830100400200
```
* 布尔值
使用t、T、true、True或TRUE 指定true。使用f、F、false、False、或FALSE指定false。
存储一个布尔值为true的field：
```
weather,location=us-midwest too_hot=true 1465839830100400200
```

参考文件：[line protocol](https://docs.influxdata.com/influxdb/v1/write_protocols/line_protocol_tutorial/#data-types)
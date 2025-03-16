# select
select column_name, column2_name from table_name;
select * from tb_name;
# select distinct
返回唯一的不同值,这里的唯一值是后续所有列组成的组合为唯一，不是指单独的列。
select distinct column1, column, ... from tb_name;
# select where
select column1, column2, ... from tb_name where condition;
## 文本字段VS数值字段
文本字段可以使用'' 或者 “” ;数值字段不用；
## where 中的条件运算符
=
<>
<
>
>=
<=
between： 在某个范围
like： 搜索某个模式
in: 指定某个列可能的多个值
# and & or
```sql
select * from websites
where country = 'CN'
and alexa > 50;
-- or
select * from websites
where country='USA'
or country='CN';
-- and & or
select * from websites
where alexa > 15
and (country='CN' or country='USA');
```
# order by 
```sql
-- 语法
-- asc 升序 默认
-- desc 降序
-- 当order by后面有多个列时，按照顺序，先按照第一列进行排序，当第一列相同时，按照第二列进行排序，以此类推；
select column1, column2, ...
from tb_name
order by column1, column2, ... asc|desc;
-- alexa asc 默认
select * from websites
order by alexa;
-- alexa desc
select * from websites
order by alexa desc;
-- 多列 multiple column
select * from websites
order by alexa, country;
```sql
# insert into
```sql
-- syntax
-- 1. no need column_name
insert into table_name values(value1, value2, value3, ...);
-- 2. need column_name
insert into table_name(column1, column2, column3, ...)
values(value1, value2, value3, ...);
-- 
insert into websites (name, url, alexa, country)
values('baidu', 'https://www.baidu.com', 4, 'CN');
-- 不完全指定所有列
-- 如下，没有指定`alexa`和id 会自动补齐
insert into websites (name, url, country)
values('stackoverflow', 'http://stackoverflow.com', 'IND');
```
# update
```sql
-- syntax
update table_name
set column1=value1, conlumn2=value2,...
where condition;
-- 
update websites
set alexa=5000, country='USA'
where name='菜鸟教程';
-- 警告：更新时，一定要有where条件，否则会全表更新
```
# delete
```sql
-- syntax
delete from tb_name
where condition
-- 
delete from websites
where name='facebook' and country='USA';
-- 删除所有数据
delete from tb_name;
```
# top, limit, rownum
```sql
-- syntax
-- number|percent 返回行数的百分比；
select top number|percent column1, column2, ...
from tb_name;
-- MySQL syntax
select column1, column2, ...
from tb_name
limit number;
-- Oracle
select column1, column2, ...
from tb_name
fetch first number rows only;
-- PG
select column1, column2, ...
from tb_name
limit number;
-- sql server ms access 返回3行数据
select top 3 employname, salary
from employees;
-- 返回10%
select top 10 percent employeename, salary
from employees;
-- mysql 返回三行
select employeename, salary
from employees
limit 3;
-- PG 返回三行
select employeename, salary
from employees
limit 3;
-- oracle
select employeename, salary
from employees
fetch first 3 rows only;
-- sql server
select top 50 percent * from websites;
```
# like operator
通常与%和_配合使用
```sql
-- syntax
select column1, column2, ...
from tb_name
where column_name like pattern;
-- 通配符
% 匹配任意字符（包括0个）
_ 匹配单个字符
-- %
select productname, category
from products
where productname like 'iphone%';
-- _
select productname, category
from products
where productname like '_e%';
-- % _
select productname, category
from products
where productname like '%zoom%';
-- 
select * 
from websites
where name like 'G%';
-- 
select *
from websites
where name like '%k';
-- 
select *
from websites
where name like '%oo%';
-- not like
select *
from websites
where name not like '%oo%';
```
# 通配符

通常与`like`关键字一起使用
% 0个或多个字符
_ 替代一个字符
[charlist] 字符列中任意一个单一字符
[^charlist]/[!charlist] 不在字符列中任意单一字符
```sql
-- 
select * 
from websites 
where url like 'https%';
-- 
select * 
from websites
where name like '_oogle';
-- ^[GFs]
-- like 与 regexp 区别
-- like： 匹配规则相对固定和简单；性能方面较高；
-- regerp：支持更多正则表达式特有的规则；性能较差
select * 
from websites
where name regexp '^[GFs]';
-- 以A-H开头的 
select *
from websites
where name regexp '^[A-H]';
-- 不以A-H开头的
select *
from websites
where name regexp '^[^A-H]';
```
# in
```sql
-- syntax
select column1, column2, ...
from tb_name
where column in (value1, value2, ...);
-- 
select *
from websites
where name in ('Google', '菜鸟教程');
```
# between
```sql
-- syntax
select column1, column2, ...
from tb_name
where column between value1 and value2;
-- 
select *
from websites
where alexa between 1 and 20;
-- not between
select *
from websites
where alexa not between 1 and 20;
```
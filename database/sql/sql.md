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
-- in + between
select *
from websites
where (alexa between 1 and 20)
and country not in ('USA', 'IND');
-- 带有文本值的between操作符实例
select * 
from websites
where name between 'A' and 'H';
-- not between
select *
from websites
where name not between 'A' and 'H';
-- 带有日期的between
select *
from access_log
where date between '2016-05-10' and '2016-05-14';
```
# 别名
```sql
-- syntax
select column_name as alias_name
from tb_name;
```
# sql别名
```sql
-- syntax
-- column alias name
select column_name as alias_name
from tb_name;
-- tb name
select column_name(s)
from tb_name as alias_name;
-- cloumn alias name
select name as n, country as c
from websites;
-- concat()
select name, concat(url, ',', alexa, ',', country) as site_info
from websites;
-- tb name
select w.name, w.url, a.count, a.date
from websites as w, access_log as a
where a.site_id=w.id and w.name="菜鸟教程";
```
# 连接（join）
```sql
-- inner join 交集
-- left join 保留左表
-- right join 保留右表
-- full outer join 并集
-- cross join 笛卡尔积（每行左表与每行右表组合）
-- self join 自身连接
-- natural join 同名字段自动匹配连接
-- syntax
select column1, column2, ...
from tb1 join tb2
on contidion;
-- inner join
select websites.id, websites.name, access_log.count, access_log.date
from websites inner join access_log
on websites.id=access_log.site_id;
```
# inner join
```sql
-- sybtax
select column_name(s)
from tb1
inner join tb2
on tb1.column_name=tb2.column_name;
-- 
select column_name(s)
from tb1
join tb2
on tb1.column_name=tb2.column_name;
-- inner join
runoob=# select students.name, enrollments.course
runoob-# from students
runoob-# inner join enrollments
runoob-# on students.studentid=enrollments.studentid;
 name  | course
-------+---------
 bob   | science
 alice | math
(2 行记录)
runoob=# select websites.name, access_log.count, access_log.date from websites inner join 
access_log on websites.id=access_log.site_id order by access_log.count;
   name   | count |    date
----------+-------+------------
 淘宝     |    10 | 2016-05-14
 微博     |    13 | 2016-05-15
 google   |    45 | 2016-05-10
 菜鸟教程 |   100 | 2016-05-13
 菜鸟教程 |   201 | 2016-05-17
 facebook |   205 | 2016-05-14
 菜鸟教程 |   220 | 2016-05-15
 google   |   230 | 2016-05-14
 facebook |   545 | 2016-05-16
(9 行记录)
```
# left join
```sql
-- syntax
select column_name(s)
from tb1
left join tb2
on tb1.column_name=tb2.column_name;
-- syntax2
select column_name(s)
from tb1
left outer join tb2
on tb1.column_name=tb2.column_name;
-- example 1
runoob=# create table customers(customerid smallint, name varchar(100));
CREATE TABLE
runoob=# insert into customers(customerid, name) values(1, 'alice'), (2, 'bob'), (3, 'charlie'), (4, 'david');
INSERT 0 4
runoob=# create table orders(orderid smallint, customerid smallint, product varchar(100));

CREATE TABLE
runoob=# insert into orders(orderid, customerid, product)values(101, 1, 'laptop'), (102, 2, 'smartphone');
INSERT 0 2
runoob=# select c.name, o.product from customers as c left join orders as o on c.customeri
d=o.customerid; 
  name   |  product
---------+------------
 alice   | laptop
 bob     | smartphone
 charlie |
 david   |
(4 行记录)
-- example2
runoob=# select w.name, a.count, a.date from websites as w left join access_log as a on w.
id=a.site_id order by a.count desc;
     name      | count |    date
---------------+-------+------------
 stackoverflow |       |
 facebook      |   545 | 2016-05-16
 google        |   230 | 2016-05-14
 菜鸟教程      |   220 | 2016-05-15
 facebook      |   205 | 2016-05-14
 菜鸟教程      |   201 | 2016-05-17
 菜鸟教程      |   100 | 2016-05-13
 google        |    45 | 2016-05-10
 微博          |    13 | 2016-05-15
 淘宝          |    10 | 2016-05-14
(10 行记录)
```
# right join
```sql
-- syntax
select column_name(s)
from tb1
right join tb2
on tb1.column_name=tb2.column_name;
-- syntax 2
select column_name(s)
from tb1
right outer join tb2
on tb1.column_name=tb2.column_name;
-- example1
runoob=# create table departments(departmentid smallint, departmentname varchar(30));
CREATE TABLE
runoob=# insert into departments(departmentid, departmentname) values(10, 'hr'), (20, 'it'
), (30, 'finance');
INSERT 0 3
runoob=# create table employees(employeeid smallint, name varchar(100), departmentid smallint);
CREATE TABLE                                                      ^
runoob=# insert into employees(employeeid, name, departmentid)values(1, 'alice', 10), (2, 'bob', 20), (3, 'charlie', null);
INSERT 0 3
runoob=# select * from employees;
 employeeid |  name   | departmentid
------------+---------+--------------
          1 | alice   |           10
          2 | bob     |           20
          3 | charlie |
(3 行记录)
runoob=# select e.name, d.departmentname from employees as e right join departments as d o
n e.departmentid=d.departmentid;
 name  | departmentname
-------+----------------
 alice | hr
 bob   | it
       | finance
(3 行记录)
-- example2
runoob=# insert into access_log(aid, site_id, count, date)values(10, 6, 111, '2016-03-09');  
INSERT 0 1
runoob=# select w.name, a.count, a.date from websites as w right join access_log as a on a
.site_id=w.id order by a.count desc;
   name   | count |    date
----------+-------+------------
 facebook |   545 | 2016-05-16
 google   |   230 | 2016-05-14
 菜鸟教程 |   220 | 2016-05-15
 facebook |   205 | 2016-05-14
 菜鸟教程 |   201 | 2016-05-17
          |   111 | 2016-03-09
 菜鸟教程 |   100 | 2016-05-13
 google   |    45 | 2016-05-10
 微博     |    13 | 2016-05-15
 淘宝     |    10 | 2016-05-14
(10 行记录)
```
# full outer join
```sql
-- syntax
select column_name(s)
from tb1
full outer join tb2
on tb1.column_name=tb2.column_name;
runoob=# create table courses(courseid smallint, studentid smallint, coursename varchar(50));
CREATE TABLE
runoob=# insert into courses(courseid, studentid, coursename) values(101, 1, 'math'), (102, 2, 'science'), (103, 4, 'history');
INSERT 0 3
runoob=# select s.studentid, s.name, c.coursename from students as s full outer join courses as c on s.studentid=c.studentid;
 studentid |  name   | coursename
-----------+---------+------------
         2 | bob     | science
         3 | charlie |
         1 | alice   | math
           |         | history
(4 行记录)
-- example2
runoob=# select w.name, a.count, a.date from websites as w full join access_log as a on w.
id=a.site_id order by a.count desc;
     name      | count |    date
---------------+-------+------------
 stackoverflow |       |
 facebook      |   545 | 2016-05-16
 google        |   230 | 2016-05-14
 菜鸟教程      |   220 | 2016-05-15
 facebook      |   205 | 2016-05-14
 菜鸟教程      |   201 | 2016-05-17
               |   111 | 2016-03-09
 菜鸟教程      |   100 | 2016-05-13
 google        |    45 | 2016-05-10
 微博          |    13 | 2016-05-15
 淘宝          |    10 | 2016-05-14
(11 行记录)
```
# union
```sql
-- syntax
-- 默认会去重，如果需要保留重复的记录，可以使用`union all`
select column1, column2, ...
from tb1
union (all)
select column1, column2, ...
from tb2;
-- example 1
runoob=# create table apps(id smallint, app_name varchar(100), url varchar(100), country varchar(30));
CREATE TABLE                                              
runoob=# insert into apps(id, app_name, url, country)values(1, 'qq app', 'http://im.qq.com', 'cn'), (2, '微博 app', 'http://weibo.com', 'cn'), (3, '淘宝 app', 'https://taobao.com', 'cn');
INSERT 0 3
-- union结果集中的列名总是等于union中第一个select语句中的列名。
runoob=# select country from websites union select country from apps order by country;
 country
---------
 cn
 ind
 usa
(3 行记录)


runoob=# select country from websites union all  select country from apps order by country
;
 country
---------
 cn
 cn
 cn
 cn
 cn
 cn
 ind
 usa
 usa
(9 行记录)
-- example 2
runoob=# select country, name from websites where country='cn' union all select country, a
pp_name from apps where country='cn' order by country;
 country |   name
---------+----------
 cn      | 淘宝
 cn      | 菜鸟教程
 cn      | 微博
 cn      | qq app
 cn      | 微博 app
 cn      | 淘宝 app
(6 行记录)
```
# select into
<!-- 从一个表中复制数据到另一个表中 -->
```sql
-- syntax
create table new_tb
as 
select * from old_tb;
-- mysql
insert into ... select ...;
-- example 1
-- 1. select into 会创建一个新表，并且新表的结构将基于选择的列和数据类型。
-- 2. 如果表已存在，select into 语句将失败。这种情况下可以使用insert into ... select 语句；
runoob=# select * into employees_backup from employees;
SELECT 3
-- example 2
runoob=# create table employees_backup_001 as select * from employees where departmentid >
= 10;
SELECT 2
runoob=# select * from employees_backup_001;
 employeeid | name  | departmentid
------------+-------+--------------
          1 | alice |           10
          2 | bob   |           20
(2 行记录)
```
# insert into select
<!-- 从一个表中复制数据到另一个已存在的表中， -->
```sql
-- syntax
insert into tb2
select * from tb1;
-- syntax 1
insert into tb2(column_name(s))
select column_name(s)
from tb1;
-- example 1
runoob=# select * from websites;
 id |     name      |            url            | alexa | country
----+---------------+---------------------------+-------+---------
  1 | google        | http://google.com         |     1 | usa
  2 | 淘宝          | https://www.taobao.com    |    13 | cn
  3 | 菜鸟教程      | https://www.runoob.com    |  4689 | cn
  4 | 微博          | https://www.weibo.com     |    20 | cn
  5 | facebook      | https://www.facebook.com  |     3 | usa
  7 | stackoverflow | https://stackoverflow.com |     0 | ind
(6 行记录)


runoob=# select * from apps;    
 id | app_name |        url         | country
----+----------+--------------------+---------
  1 | qq app   | http://im.qq.com   | cn
  2 | 微博 app | http://weibo.com   | cn
  3 | 淘宝 app | https://taobao.com | cn
(3 行记录)


runoob=# insert into websites(name, country) select app_name, country from apps;
INSERT 0 3
runoob=# select * from websites;
 id |     name      |            url            | alexa | country
----+---------------+---------------------------+-------+---------
  1 | google        | http://google.com         |     1 | usa
  2 | 淘宝          | https://www.taobao.com    |    13 | cn
  3 | 菜鸟教程      | https://www.runoob.com    |  4689 | cn
  4 | 微博          | https://www.weibo.com     |    20 | cn
  5 | facebook      | https://www.facebook.com  |     3 | usa
  7 | stackoverflow | https://stackoverflow.com |     0 | ind
    | qq app        |                           |       | cn
    | 微博 app      |                           |       | cn
    | 淘宝 app      |                           |       | cn
(9 行记录)
-- example 2
runoob=# select * from websites;
 id |     name      |            url            | alexa | country
----+---------------+---------------------------+-------+---------
  1 | google        | http://google.com         |     1 | usa
  2 | 淘宝          | https://www.taobao.com    |    13 | cn
  3 | 菜鸟教程      | https://www.runoob.com    |  4689 | cn
  4 | 微博          | https://www.weibo.com     |    20 | cn
  5 | facebook      | https://www.facebook.com  |     3 | usa
  7 | stackoverflow | https://stackoverflow.com |     0 | ind
    | qq app        |                           |       | cn
    | 微博 app      |                           |       | cn
    | 淘宝 app      |                           |       | cn
(9 行记录)


runoob=# select * from apps;                                                              
 id | app_name |        url         | country
----+----------+--------------------+---------
  1 | qq app   | http://im.qq.com   | cn
  2 | 微博 app | http://weibo.com   | cn
  3 | 淘宝 app | https://taobao.com | cn
(3 行记录)


runoob=# insert into websites(name, country) select app_name, country from apps where id=1
;
INSERT 0 1
runoob=# select * from websites;                                                          
 id |     name      |            url            | alexa | country
----+---------------+---------------------------+-------+---------
  1 | google        | http://google.com         |     1 | usa
  2 | 淘宝          | https://www.taobao.com    |    13 | cn
  3 | 菜鸟教程      | https://www.runoob.com    |  4689 | cn
  4 | 微博          | https://www.weibo.com     |    20 | cn
  5 | facebook      | https://www.facebook.com  |     3 | usa
  7 | stackoverflow | https://stackoverflow.com |     0 | ind
    | qq app        |                           |       | cn
    | 微博 app      |                           |       | cn
    | 淘宝 app      |                           |       | cn
    | qq app        |                           |       | cn
(10 行记录)
```
# create database
```sql
-- syntax
create database dbname;
-- example 1
runoob=# \l
                                                                              数据库列表 
   名称    |  拥有者  | 字元编码 | Locale Provider |            校对规则            |             Ctype              | ICU Locale | ICU Rules |       存取权限
-----------+----------+----------+-----------------+--------------------------------+--------------------------------+------------+-----------+-----------------------
 mydb      | postgres | UTF8     | libc            | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |            |           |
 postgres  | postgres | UTF8     | libc            | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |            |           |
 runoob    | postgres | UTF8     | libc            | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |            |           |
 template0 | postgres | UTF8     | libc            | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |            |           | =c/postgres          +
           |          |          |                 |                                |                                |            |           | postgres=CTc/postgres
 template1 | postgres | UTF8     | libc            | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |            |           | =c/postgres          +
           |          |          |                 |                                |                                |            |           | postgres=CTc/postgres
(5 行记录)


runoob=# create database runoob_mydb;
CREATE DATABASE
runoob=# \l
                                                                               数据库列表
    名称     |  拥有者  | 字元编码 | Locale Provider |            校对规则            |             Ctype              | ICU Locale | ICU Rules |       存取权限
-------------+----------+----------+-----------------+--------------------------------+--------------------------------+------------+-----------+-----------------------
 mydb        | postgres | UTF8     | libc            | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |            |           |
 postgres    | postgres | UTF8     | libc            | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |            |           |
 runoob      | postgres | UTF8     | libc            | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |            |           |
 runoob_mydb | postgres | UTF8     | libc            | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |            |           |
 template0   | postgres | UTF8     | libc            | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |            |           | =c/postgres          +
             |          |          |                 |                                |                                |            |           | postgres=CTc/postgres
 template1   | postgres | UTF8     | libc            | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |            |           | =c/postgres          +
             |          |          |                 |                                |                                |            |           | postgres=CTc/postgres
(6 行记录)
```
# create table
```sql
-- syntax
create table tb_name
(
    column_name1 data_type(size),
    column_name2 data_type(size),
    ...
);
-- example 1
runoob=# \d
                      关联列表
 架构模式 |         名称         |  类型  |  拥有者  
----------+----------------------+--------+----------
 public   | access_log           | 数据表 | postgres
 public   | apps                 | 数据表 | postgres
 public   | courses              | 数据表 | postgres
 public   | customers            | 数据表 | postgres
 public   | departments          | 数据表 | postgres
 public   | employees            | 数据表 | postgres
 public   | employees_backup     | 数据表 | postgres
 public   | employees_backup_001 | 数据表 | postgres
 public   | enrollments          | 数据表 | postgres
 public   | orders               | 数据表 | postgres
 public   | students             | 数据表 | postgres
 public   | websites             | 数据表 | postgres
(12 行记录)


runoob=# create table persons(personid int, lastname varchar(255), firstname varchar(255), address varchar(255), city varchar(255));
CREATE TABLE
runoob=# \d
                      关联列表
 架构模式 |         名称         |  类型  |  拥有者
----------+----------------------+--------+----------
 public   | access_log           | 数据表 | postgres
 public   | apps                 | 数据表 | postgres
 public   | courses              | 数据表 | postgres
 public   | customers            | 数据表 | postgres
 public   | departments          | 数据表 | postgres
 public   | employees            | 数据表 | postgres
 public   | employees_backup     | 数据表 | postgres
 public   | employees_backup_001 | 数据表 | postgres
 public   | enrollments          | 数据表 | postgres
 public   | orders               | 数据表 | postgres
 public   | persons              | 数据表 | postgres
 public   | students             | 数据表 | postgres
 public   | websites             | 数据表 | postgres
(13 行记录)
```
# 约束
```sql
-- syntax
create table tb_name
(
    column1 data_type(size) constraint_name,
    column2 data_type(size) constraint_name,
    ...
);
-- constraint name
not null
unique 唯一值
primary key - 相当于是not null 和unique的结合，主键
foreign key - 保证一个表中的数据匹配另一个表中的值，参照完整性
check - 保证列中的值复合指定条件
default - 规定没有值时的默认值
index - 用于快速访问数据库表中的数据
-- example 1 not null
runoob=# create table students_001(studentid int not null, lastname varchar(50) not null, firstname varchar(50), age int);
CREATE TABLE
runoob=# insert into students_001(age) values(29);
-- 错误:  null value in column "studentid" of relation "students_001" violates not-null constraint
-- 描述:  失败, 行包含(null, null, null, 29).
runoob=# insert into students_001(studentid, age) values(1, 29);
-- 错误:  null value in column "lastname" of relation "students_001" violates not-null constraint
-- 描述:  失败, 行包含(1, null, null, 29).
runoob=# insert into students_001(studentid, lastname,  age) values(1,'baker', 29);
INSERT 0 1
-- example 2 unique
runoob=# create table employees_001(employeeid int not null unique, lastname varchar(50) n
ot null, firstname varchar(50), email varchar(100) unique);
CREATE TABLE
runoob=# insert into employees_001(employeeid, lastname, firstname, email)values(1, 'x', 'baker', '111@123.com');
INSERT 0 1
runoob=# insert into employees_001(employeeid, lastname, firstname, email)values(1, 'x1', 
'baker1', '111@123.com');
-- 错误:  重复键违反唯一约束"employees_001_employeeid_key"
-- 描述:  键值"(employeeid)=(1)" 已经存在
-- example 3 primary key
runoob=# create table orders001(doderid int not null primary key, ordernumber int not null
, orderdate date not null);
CREATE TABLE
-- example 4 foreign key
runoob=# create table orders_002(orderid int not null primary key, ordernumber int not null, customerid int, foreign key(customerid) references customers(customerid));
-- 错误:  没有唯一约束与关联表 "customers" 给定的键值匹配
runoob=# alter table customers add primary key(customerid);
ALTER TABLE
runoob=# create table orders_002(orderid int not null primary key, ordernumber int not null, customerid int, foreign key(customerid) references customers(customerid));
CREATE TABLE
-- 5. check
-- 确保列中的值满足特定条件
runoob=# create table products_001(productid int not null primary key, productname varchar(100) not null, price decimal(10, 2) check(price >= 0));
CREATE TABLE
-- 6. default
runoob=# create table customers_002(customerid int not null primary key, lastname varchar(50) not null, firstname varchar(50), joindate date default now());    
CREATE TABLE
-- 7. index
runoob=# create index idx_lastname on employees(employeeid);
CREATE INDEX
```
# not null
```sql
-- example 1
runoob=# create table persons_001(id int not null, lastname varchar(255) not null, firstna
me varchar(255) not null, age int);
CREATE TABLE
runoob=# alter table persons_001 alter column age set  not null;
ALTER TABLE
runoob=# alter table persons_001 alter column age drop   not null;
ALTER TABLE
runoob=# \d persons_001
                   数据表 "public.persons_001"
   栏位    |          类型          | 校对规则 |  可空的  | 预设
-----------+------------------------+----------+----------+------
 id        | integer                |          | not null |
 lastname  | character varying(255) |          | not null |
 firstname | character varying(255) |          | not null |
 age       | integer                |          |          |
```
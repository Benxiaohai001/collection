select * from t1 where c1 > 42 limit 10
select * from t1 order by c1 limit 10
select * from t1 order by c1 limit 10;

# dql
## like
用于在where子句中；
# 链表查询
## 内连接（INNER JOIN）
学生表：ID，姓名；
成绩表：ID，成绩；
```sql
select * from students inner join score on students.id = score.id;
```
## 左连接
左边所有行及右边满足条件的行，若右表无匹配行，则结果中添加null。
```sql
select * from student left join score on student.id = score.id;
```
## 右连接
与左相反
## 全连接
左右的并集；不存在的补充null
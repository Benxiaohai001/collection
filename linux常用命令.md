# awk 
awk -F "," '{print NF}'  统计每行列数，以 ‘，’ 分割
# crontab
-e 编辑定时任务;定时任务日志：Var/log/cron
# command: 执行一个简单的命令，或者打印命令的相关信息
-p
-V
-v
# dmesg:显示（display message）开机信息
-T 使用人类方便读取的时间戳格式
# env 展示系统环境变量
# filefrag 文件分片报告
-e：已区段段形式打印，块映射文件
# fio 灵活的IO测试
## 模拟坏块 fio --name=badblock --ioengine=sync --rw=write --bs=4k --numjobs=1 --size=1G --filename=/dev/sdb --offset=1G --direct=1 --invalidate=1 --verify=0 --exitall
这个命令会在/dev/sdb磁盘的第2GB位置创建一个坏块。使用这个命令需要小心，因为它会直接在磁盘上进行操作，并可能导致数据丢失和硬件损坏。
## 模拟磁盘故障 fio --name=crash --ioengine=sync --rw=write --bs=4k --numjobs=1 --size=1G --filename=/dev/sdb --direct=1 --invalidate=1 --verify=0 --do_verify=1 --verify_fatal=1 --exitall
这个命令会在/dev/sdb磁盘上写入1GB数据，然后立即关闭磁盘。这样会导致数据丢失和文件系统损坏。
name: job的名字
ioengine: io引擎；default：psync，sync，vsync。。。。。
rw：io指令；default：read
bs： 块大小 default：4096
numjobs: 将此操作重复多次 default：1
size： 文件或设备大小；
filename：工作负载的文件
offset：从哪里开始io default：0
direct：使用O_DIRECT读取；default：0
invalidate：在运行作业之前使缓冲区/页面缓存无效 default：1
verify：验证数据写 default：0
exitall：一旦退出终止所有任务
offset:开始io的偏移量


### 相关概念
#### psync/sync/vsync/psynv2
read pread readv preadv2：主要全部都是从文件中读取数据，不同在于读取的偏移量和读取方式不同；
write pwrite writev pwritev pwritev2：都是linux/unix中向文件中写入数据的函数，不同之处在写入方式和偏移量不同
#### O_DIRECT
lunix/unix中的函数，可以跳过内核缓存直接读取磁盘文件
# free 检查内存
-h
# head  显示开始的几行
-n 指定行数
# hexdump: linux下二进制查看工具
# iostat -xt 2 检查磁盘io速率
# journalctl：用来查询 systemd-journald 服务收集到的日志。
# local: 在函数内部定义局部变量
# lsblk: 展示所有可用的或者指定的块设备（磁盘）
展示磁盘的maj：min  
maj表示不同的设备；
min表示不同的分区
# lscpu 展示cpu信息
# lsscsi ： 展示scsi设备和相关属性
-l 输出每个scsi设备的附加信息
# make& cmake 

makefile：具体的构建规则；
make编译出现如下错误时，修改cmakelist。txt文件；这里是把部分警告信息作为error输出了


# maven 项目管理/测试工具
# more 与cat类似，不过会一页一页的展示数据；
# rpm:
 -e 擦除，卸载
ivh
# rsync 同步文件
# sed 修改文件
-i “s/oldstring/newstring/g” xxx.txt
-i "1i xxxx" xxx.txt   文件中第一行插入一行；
-i "s/指定字符串/&之后添加字符串/" /tmp/test.txt
-i "s/指定字符串/之前添加字符串&/" /tmp/test.txt
-i "/xxx/d" xxx.txt 删除包含指定字符串的行
# set:设置shell的不同执行方式
-e 如果shell返回结果不是0，立即退出shell
# sort :对文档进行排序
# systemctl 查询或者发送控制命令到systemd manager
管理声明周期命令
# daemon-reload重新加载系统配置
# tar 
-C 解压到指定目录
-o pipefail 管道中间有有非零返回值，直接返回；
# top
-p 监控具体的进程
# time: 计算命令执行的时间
# ulimit:
-a 显示相关设置信息
-n xxx  设置句柄
-c unlimited 设置生成core文件；
# uname  显示系统必要信息
-a 打印所有信息
-r 打印内核信息
-n 打印节点名称
# uniq：过滤重复的行
-d：仅显示重复的行，不进行删除；
# vim/vi:
命令模式：
$ 跳到本行末尾
0 跳到本行开头
普通模式：
写入模式：
批量替换： :%s/oldstring/newstring/g 
批量注释
打开文件
v进入visual模式
上下键选择注释的行
control+v进入块选择模式，
大写“I”进入插入模式，
输入 # 或者//
点击两下 esc键，即可以批量注释
批量取消注释
打开文件
control + v进入块选择模式；
上下键选择需要取消注释的内容；
点击d 取消注释
# who 打印当前登陆的用户
# wget 非交互式文件下载工具
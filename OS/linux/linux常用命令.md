# arch
显示当前环境cpu架构
# awk 
awk -F "," '{print NF}'  统计每行列数，以 ‘，’ 分割 \
awk '{print $2}' 以空格分隔，打印第二个 \
awk '{if (gsub(/ /,"&") != 2) print NR, $0}' line_protocol/cnodb-iot-seed-123-scale-100-2021_001 判断文件中哪一行没有两个空格
# crontab
-e 编辑定时任务;定时任务日志：Var/log/cron
# command: 执行一个简单的命令，或者打印命令的相关信息
-p
-V
-v
# curl 与服务端传输数据
* -I, --head
仅获取请求头
* -s, --silent
静默或退出模式
* -w, --write-out <format>
请求完成之后将返回内容输出到标准输出
# dd 复制文件，转换格式等
bs 每次读写多少文件 \
if 读取的文件 \
of 写入的文件 \
count 只复制前N个块
# dirname 输出当前文件所在目录
dirname "$0" 输出执行脚本的目录
# dmesg:显示（display message）开机信息
-T 使用人类方便读取的时间戳格式
# env 展示系统环境变量
# filefrag 文件分片报告
-e：已区段段形式打印，块映射文件
# fio 灵活的IO测试
## 常用故障命令
### 模拟坏块 fio --name=badblock --ioengine=sync --rw=write --bs=4k --numjobs=1 --size=1G --filename=/dev/sdb --offset=1G --direct=1 --invalidate=1 --verify=0 --exitall
这个命令会在/dev/sdb磁盘的第2GB位置创建一个坏块。使用这个命令需要小心，因为它会直接在磁盘上进行操作，并可能导致数据丢失和硬件损坏。
### 模拟磁盘故障 fio --name=crash --ioengine=sync --rw=write --bs=4k --numjobs=1 --size=1G --filename=/dev/sdb --direct=1 --invalidate=1 --verify=0 --do_verify=1 --verify_fatal=1 --exitall
这个命令会在/dev/sdb磁盘上写入1GB数据，然后立即关闭磁盘。这样会导致数据丢失和文件系统损坏。\
## 子命令
name: job的名字 \
ioengine: io引擎；default：psync，sync，vsync。。。。。\
rw：io指令；default：read \
bs： 块大小 default：4096 \
numjobs: 将此操作重复多次 default：1 \
size： 文件或设备大小； \
filename：工作负载的文件 \
offset：从哪里开始io default：0 \
direct：使用O_DIRECT读取；default：0 \
invalidate：在运行作业之前使缓冲区/页面缓存无效 default：1 \
verify：验证数据写 default：0 \
exitall：一旦退出终止所有任务 \
offset:开始io的偏移量 \
## 报告解读
### slat
指将I/O请求提交到系统队列中所需的时间，以纳秒为单位。这个时间包括了I/O请求在fio的I/O引擎中排队等待的时间、以及将请求提交到系统队列中的时间。
### clat
指从I/O请求提交到系统队列中开始，到I/O请求完成所需的时间，以纳秒为单位。这个时间包括了I/O请求在系统队列中排队等待的时间、以及磁盘读写操作完成的时间。


## 相关概念
#### psync/sync/vsync/psynv2
read pread readv preadv2：主要全部都是从文件中读取数据，不同在于读取的偏移量和读取方式不同；
write pwrite writev pwritev pwritev2：都是linux/unix中向文件中写入数据的函数，不同之处在写入方式和偏移量不同
#### O_DIRECT
lunix/unix中的函数，可以跳过内核缓存直接读取磁盘文件
# fdisk 磁盘增加分区
fdisk 磁盘分区最多2T；如果磁盘分区要求大于2T，可以使用parted
# find
find /home/user -type d -name "my_folder"  查找指定名称的目录位置 \
# free 检查内存
-h
# head  显示开始的几行
-n 指定行数
# hexdump: linux下二进制查看工具
# iostat -xt 2 检查磁盘io速率 
# iotop 检查io速率
# journalctl：用来查询 systemd-journald 服务收集到的日志。
## 检查某个时间段的日志
sudo journalctl --since "2025-07-17 01:40" --until "2025-07-17 02:05"
# kill 发送信号到进程
## 常见的信号
```shell
[user2@pc] kill -l 9
KILL
kill SIGSEGV/11 pid # 使进程crash
kill SIGABRT/6 pid # 使进程crash

# 列出所有信号名称：
[user2@pc] kill -l
 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL
 5) SIGTRAP      6) SIGABRT      7) SIGBUS       8) SIGFPE
 9) SIGKILL     10) SIGUSR1     11) SIGSEGV     12) SIGUSR2
13) SIGPIPE     14) SIGALRM     15) SIGTERM     16) SIGSTKFLT
17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU
25) SIGXFSZ     26) SIGVTALRM   27) SIGPROF     28) SIGWINCH
29) SIGIO       30) SIGPWR      31) SIGSYS      34) SIGRTMIN
35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3  38) SIGRTMIN+4
39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12
47) SIGRTMIN+13 48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14
51) SIGRTMAX-13 52) SIGRTMAX-12 53) SIGRTMAX-11 54) SIGRTMAX-10
55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7  58) SIGRTMAX-6
59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
63) SIGRTMAX-1  64) SIGRTMAX

# 下面是常用的信号。
# 只有第9种信号(SIGKILL)才可以无条件终止进程，其他信号进程都有权利忽略。

HUP     1    终端挂断
INT     2    中断（同 Ctrl + C）
QUIT    3    退出（同 Ctrl + \）
KILL    9    强制终止
TERM   15    终止
CONT   18    继续（与STOP相反，fg/bg命令）
STOP   19    暂停（同 Ctrl + Z）

```

# killall 通过名称kill所有相关进程
## centos下载时使用命令
```bash
yum install psmisc
而不是
yum install killall
```
# ldconfig
运行时配置动态链接库
# local: 在函数内部定义局部变量
# lsblk: 展示所有可用的或者指定的块设备（磁盘）
展示磁盘的maj：min  
maj表示不同的设备；
min表示不同的分区
lsblk -d -o name,rota # rote为1表示hdd，rote为0表示sdd
# lscpu 展示cpu信息
# lsof 展示打开的文件数和网络连接数
-p pid 展示之指定进程的打开文件和网路链接数量
## 怎么区分网络连接和文件
如果 TYPE 列的值为 IPv4、IPv6、TCP、UDP、UNIX 或 unix 等，表示该行记录是一个网络连接；如果 TYPE 列的值为 REG、DIR、FIFO、CHR、BLK 或 LINK 等，表示该行记录是一个打开的文件。
# lsscsi ： 展示scsi设备和相关属性
-l 输出每个scsi设备的附加信息
# make& cmake 

makefile：具体的构建规则；
make编译出现如下错误时，修改cmakelist。txt文件；这里是把部分警告信息作为error输出了


# maven 项目管理/测试工具
# more 与cat类似，不过会一页一页的展示数据；
# parted
parted /dev/sdc mklabel gpt 添加标签 \
parted /dev/sdc mkpart primary ext4 0% 100% 制作分区 \
# rpm:
 -e 擦除，卸载
ivh
# rsync 同步文件
# sed 修改文件
-i “s/oldstring/newstring/g” xxx.txt \
-i "1i xxxx" xxx.txt   文件中第一行插入一行； \
-i "s/指定字符串/&之后添加字符串/" /tmp/test.txt \
-i "s/指定字符串/之前添加字符串&/" /tmp/test.txt \
sed -i "s/>/\&&/" run_cluster.sh 如果字符串中有特殊字符&用反斜杠转意 \
-i "/xxx/d" xxx.txt 删除包含指定字符串的行 \
sed -i '1d' line_protocol/cnodb-iot-seed-123-scale-100-2021_001 删除第1行字符串
# set:设置shell的不同执行方式
-e 如果shell返回结果不是0，立即退出shell \
+e 如果返回的结果不是0，程序可以继续执行
# shift:
shift命令可以用于向左移动命令行参数。它将当前的命令行参数列表向左移动一个位置，并将第一个参数丢弃。这意味着，$2现在变成了$1，$3现在变成了$2，以此类推。
# shuf 
将输入的随机打乱顺序输出到标准输出中
# sort :对文档进行排序
# source：
设置环境变量；\
shell 脚本中 source filename表示执行一个脚本
# systemctl 查询或者发送控制命令到systemd manager
管理声明周期命令
systemctl daemon-reload // 更新配置

systemctl start node_exporter
systemctl status node_exporter
systemctl enable node_exporter  开机启动；
systemctl disable node_exporter // 取消开机启动

# tcpdump
tcpdump -i any -A 'tcp port 8902 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'
获取指定端口被访问api

# daemon-reload重新加载系统配置
# tar 
-C 解压到指定目录
-o pipefail 管道中间有有非零返回值，直接返回；
# top
-p 监控具体的进程
# trap 捕捉信号或事件并执行命令

# time: 计算命令执行的时间
# tree 树形结构展示目录下的文件和目录
# ulimit:
-a 显示相关设置信息
-n xxx  设置句柄
-c unlimited 设置生成core文件；
# uname  显示系统必要信息
-a 打印所有信息
-r 打印内核信息
-n 打印节点名称
-m 打印当前节点cpu系统架构
# uniq：过滤重复的行
-d：仅显示重复的行，不进行删除；
# vim/vi:
## 取消行号
:set nonu
## 命令模式：
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
# ifconfig centos系统  使用yum下载 sudo yum install net-tools  net-tools 包含ifconfig命令
# 包管理工具：cnetos  yum;ubuntu:apt;
# 常见特殊符号
$# 表示参数的个数
$@ 表示参数的内容
# 快捷键
control + k 删除光标之后的所有字符串数据；\
control + u 删除光标之前的所有字符串数据；\
磁盘：
echo -e "\033[?25l"  隐藏光标echo -e "\033[?25h" 显示光标
# 生成coredump：
# 升级gcc到指定版本
yum install devtoolset-11 -y \
yum install devtoolset-11 -y \
echo "source /opt/rh/devtoolset-11/enable" >> /etc/profile \
source /etc/profile \
yum install openssl openssl-devel \
目录
# linux中常见的目录盘符
## proc 目录:保存运行时的部分基本信息
提供系统内核运行时的信息。/proc 目录下的文件和子目录实际上并不是真实的文件和目录，而是在内核运行时动态生成的，它们提供有关系统内核、进程、设备和网络等方面的信息。 \
### /proc/cpuinfo：包含了 CPU 的信息，如型号、速度、缓存等等。
### /proc/meminfo：包含了系统内存的信息，如总内存、可用内存、缓存等等。
### /proc/filesystems：包含了支持的文件系统类型的列表。
### /proc/loadavg：包含了系统的平均负载，即过去 1 分钟、5 分钟、15 分钟内的平均进程数。
### /proc/net：包含了网络相关的信息，如网络接口、TCP 和 UDP 连接等等。
### /proc/sys：包含了内核参数的信息，可以用来设置和查询内核参数的值。
### /proc/<PID>：包含了某个进程的信息，如进程的状态、命令行参数、打开的文件、网络连接等等。
## >/dev/null 2>&1 ：将所有的标准输出和错误输出全部输出到 dev null 
devnull 在Linux和unix系统中表示信息黑洞，任何数据都可以指向他，\
0 表示标准输入 \
1表示标准输出 \
2表示标准错误输出 
## /dev/zero: 是linux中的一个特殊设备字符文件，可以从中读取无限量的零字节。
# 文件系统
## extents
extents 是文件系统中的一个概念，表示文件在磁盘上的分布情况。当一个文件很大的时候，文件系统会把它分成多个块存储在磁盘上。每个块被称为一个 extent，其中包含了若干个连续的磁盘块。这样做的好处是可以更好地利用磁盘空间，同时也可以提高文件的读写效率。

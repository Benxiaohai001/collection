# shebang
#!/sur/bin/env 
shebang寻找时和和alias会冲突，shebang会直接从操作系统PATH中寻找可执行的二进制文件，不会直接使用alias的文件
# 管道 ｜
用于命令之间数据流动；
标准输出｜标准输入：将上一个命令的标准输出作为下一个命令的标准输入；
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
# 清理缓存
'''bash
echo 1 > /proc/sys/vm/drop_caches
'''
# swap
在Linux操作系统中，"swap" 是指用于虚拟内存管理的一种机制。虚拟内存是一种将计算机的物理内存和硬盘空间结合起来使用的技术，允许操作系统将部分内存中的数据临时存储到硬盘上，以释放物理内存供其他程序使用。
# cpu&mem 分别在什么情况下会使用相应的资源？
系统资源的占用情况涉及到多个因素，包括进程的需求、系统调度策略、应用程序设计等。下面是一些常见的情况，描述了在什么情况下会占用 CPU 和内存：
## 占用 CPU 的情况：
* 运行计算密集型任务：当程序需要进行大量的计算、处理复杂算法或执行大量的循环时，会占用较多的 CPU 资源。
* 并发处理：当系统中有多个并发任务需要执行时，每个任务都需要一定的 CPU 时间片来运行，从而占用 CPU 资源。
* 实时响应：某些任务要求实时响应，例如图形渲染、音视频处理等，这些任务需要连续不断地处理数据并及时响应用户输入，因此会占用较多的 CPU 资源。
## 占用内存的情况：
* 分配大量数据：当程序需要处理大量的数据，例如加载大型文件、操作大型数据集或执行复杂的数据处理任务时，会占用较多的内存资源。
* 缓存数据：应用程序可能会将某些数据缓存在内存中，以提高访问速度。这些缓存数据会占用一定的内存空间。
* 并发进程：每个进程都需要分配一定的内存空间来存储其执行环境和数据。当系统中有多个并发进程时，会占用较多的内存资源。
* 内存泄漏：如果应用程序存在内存泄漏问题，即分配的内存无法释放，那么随着时间的推移，内存占用会不断增加，最终导致内存耗尽。
需要注意的是，CPU 和内存的占用情况通常是动态变化的，取决于系统运行的具体任务和应用程序的需求。对于性能敏感的应用程序，合理优化和管理 CPU 和内存资源是很重要的，以确保系统的稳定性和性能表现。

# signal 11 空指针

# 清理未删除句柄
lsof | grep deleted | awk '{print $2, $3}' | while read pid fd; do kill -9 $pid; done

# EOF
EOF在shell中是一个特殊的标记，用于表示一段文字的结束。它通常与cat命令一起使用，用于将多行文本输出到文件或终端。EOF可以自定义为其他名称，如EEE、MAMA等。
使用EOF的示例：
```shell
bash
cat <<EOF >test.txt
hello
world
EOF
```
上述命令将"hello"和"world"两行文本输出到test.txt文件中。EOF标记了文本输入的结束。

# 系统目录
## /usr/lib/systemd/system/
目录 /usr/lib/systemd/system/ 是 systemd 的 unit 的配置文件位置。
在这个目录下，系统可以找到所有的服务单元配置文件。

当使用 systemctl daemon-reload 命令时，它会重新加载这个目录下的所有配置文件，以确保服务单元的配置是最新的。这对于新安装或修改的服务来说非常重要，因为它们的服务程序配置文件需要生效才能被系统正确地管理和控制

## /var/lib/dpkg/status
/var/lib/dpkg/status 是 Ubuntu 系统中的一个文件，它存储了关于已安装软件包的信息和元数据。该文件包含了每个已安装软件包的详细信息，如软件包名称、版本号、依赖关系、安装状态等。
/var/lib/dpkg/status 文件是由 dpkg 软件包管理工具维护和更新的，它用于跟踪和管理系统中已安装的软件包。当你使用 dpkg 或 apt 等工具进行软件包操作时，这个文件将被读取和更新
通常情况下，你不需要直接编辑 /var/lib/dpkg/status 文件。它由 dpkg 和相关工具负责管理。如果你需要查看已安装软件包的信息，可以使用 dpkg 命令或其他软件包管理工具。
例如，要查看 /var/lib/dpkg/status 文件中所有已安装软件包的列表，可以运行以下命令：
dpkg --list
该命令将显示已安装软件包的列表，包括软件包名称、版本号和状态等信息。
请注意，对 /var/lib/dpkg/status 文件的任何更改都应该非常小心，并且最好由软件包管理工具来处理。误操作或不正确的更改可能导致系统中的软件包状态不一致或损坏。

## /var/lib/dpkg/lock-frontend
/var/lib/dpkg/lock-frontend 是 Ubuntu 系统中的一个文件，用于实现对软件包管理器 (dpkg) 的并发访问控制。当有其他进程正在使用 dpkg 或 apt 工具时，该文件会被锁定，以防止多个进程同时进行软件包操作。
该文件的存在表示有其他进程正在进行软件包管理操作，例如正在进行软件包安装、更新或删除等操作。当你尝试运行 apt 或 dpkg 命令时，如果无法获取到锁定文件，就会出现类似的错误信息。
这是为了确保在进行软件包操作时不会发生冲突或损坏。锁定文件的存在告诉你当前有其他进程正在进行软件包管理操作，因此你需要等待操作完成或者确定是否存在其他问题。
如果你确定没有其他进程正在使用 dpkg 或 apt 工具，但仍然无法找到 /var/lib/dpkg/lock-frontend 文件，可能是由于文件被意外删除或其他异常情况。在这种情况下，你可以尝试重新创建锁定文件：
```bash
sudo touch /var/lib/dpkg/lock-frontend
sudo chmod 644 /var/lib/dpkg/lock-frontend
```
这将创建一个空的锁定文件并设置适当的权限。然后，你可以尝试再次运行软件包管理命令。
如果问题仍然存在，可能需要进一步检查系统的状态，并确保没有其他进程在进行软件包操作。

* 清空nohup.out，后续进程还可以写入数据，但是不会删除nohup.out文件
:>nohup.out
# epel
EPEL(Extra Packages for Enterprise Linux)
# 文件类型
s：套接字文件
# 证书
openssl
## 检查证书支持的IP
openssl x509 -noout -text -in /etc/kubernetes/pki/apiserver.crt | grep "IP Address"
## tip
### crt文件
证书文件
### key文件
私钥文件
# 文件压缩
||tar.gz|tar.xz|
|---|---|---|
|压缩算法|gzip|lzma/xz|
|压缩速度|***快|*慢|
|压缩率|中等|极高(比gzip高约30%)|
|解压速度|***快|*较慢|
|cpu/内存|较低|较高|
|通用型|极高|较新|
|典型扩展名|.tar.gz,.tgz|.tar.xz,txz|
|压缩|tar zcvf file.tar.gz dir|tar -cJvf file.tar.xz dir|
|解压|tar -zxvf file.tar.gz| tar xJvf file.tar.xz|
ifconfig centos系统  使用yum下载 sudo yum install net-tools  net-tools 包含ifconfig命令
包管理工具：cnetos  yum;ubuntu:apt;
$# 表示参数的个数
$@ 表示参数的内容
control + k 删除光标之后的所有字符串数据；
control + u 删除光标之前的所有字符串数据；
磁盘：
echo -e "\033[?25l"  隐藏光标echo -e "\033[?25h" 显示光标
生成coredump：
升级gcc到指定版本
yum install devtoolset-11 -y
yum install devtoolset-11 -y
echo "source /opt/rh/devtoolset-11/enable" >> /etc/profile
source /etc/profile
yum install openssl openssl-devel
目录
proc 目录:保存运行时的部分基本信息
 >/dev/null 2>&1 ：将所有的标准输出和错误输出全部输出到 dev null 
devnull 在Linux和unix系统中表示信息黑洞，任何数据都可以指向他，
0 表示标准输入
1表示标准输出
2表示标准错误输出
虚拟机启动之后可能网络不能直接连接到公司内网。
需要进行如下操作
```bash
set -ex 
# 创建一个新的网络设备
ip link add br0 type bridge 
# 启用这个接口
ifconfig br0 up
# 将物理网口于该接口绑定 
ip link set enP4s2f1 master br0 
sleep 1 
# 为br0配置ip
ip address add dev br0 10.24.10.26/23 
sleep 1 
# 设置默认网关
ip route add default via 10.24.10.1 dev br0
```
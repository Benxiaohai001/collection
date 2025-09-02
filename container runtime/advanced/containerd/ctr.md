# ctr
ctr 是一个不受支持的调试和管理客户端，用于与 containerd 守护进程交互。由于它不受支持，因此无法保证其命令、选项和操作在 containerd 项目的各个版本之间向后兼容或稳定。
## c 管理容器
ls
rm

## i 检查镜像
ls
rm
## task(t)管理任务
delete,del, rm
exec
kill 停止一个容器
ls
start 启动
```sh
ctr task exec --exec-id <唯一ID> -t <容器名称> <命令>
ctr task exec --exec-id sh1 -t test /bin/sh
```
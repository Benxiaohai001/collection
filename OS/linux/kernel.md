[linux kernel](https://www.kernel.org/)
# cgroup
## 功能
资源限制，优先级分配，资源统计和隔离。
```bash
stat -fc %T /sys/fs/cgroup # 检查文件系统类型，
1. cgroup2fs表示cgroup v2
2. tmpfs表示是cgroup v1
```
# service与systemctl区别
|对比维度|service（传统）|systemctl（现代命令）|
|---|---|---|
|所属初始化系统|sysvinit或upstart|systemd|
|管理方式|通过/etc/init.d/目录下的脚本|通过读取/etc/systemd/system/目录下的service单元文件|
|功能范围|基本操作：启动，停止，重启，查看状态|功能全面：除基本操作外，还包括开机自启动/金庸，详细状态查看，日志管理，资源控制等|
|启动方式|顺序启动，速度较慢|并行启动，大幅提升系统启动速度|
|依赖管理|依赖关系在脚本内手动处理，较为简单|自动解析和管理服务之间的依赖关系，更可靠|
|适用命令|service <服务名> start/stop/restart/status| systemctl start/stop/restart/status <服务名>|

[linux kernel](https://www.kernel.org/)
# cgroup
## 功能
资源限制，优先级分配，资源统计和隔离。
```bash
stat -fc %T /sys/fs/cgroup # 检查文件系统类型，
1. cgroup2fs表示cgroup v2
2. tmpfs表示是cgroup v1
```
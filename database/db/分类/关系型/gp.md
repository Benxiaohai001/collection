# 部署安装
https://techdocs.broadcom.com/us/en/vmware-tanzu/data-solutions/tanzu-greenplum/7/greenplum-database/install_guide-init_gpdb.html
1. 所有节点建立互信
2. 修改配置文件 gpinitsystem_config
```config
COORDINATOR_HOSTNAME 改成master节点hostname；其他参数可以使用默认的，使用三个节点搭建集群
```
3. 编写集群节点hostname
```bash
4dd4e834aee5
f078031796d9
0501720c3886
```
4. 各节点创建相应目录（注意权限）
5. 启动
```bash
gpinitsystem -c ./gpinitsystem_config -h hostfile_gpinitsystem
```
## 备注
修改配置，不用重启，可以使用`gpstop -u` 加载配置
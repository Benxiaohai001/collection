# subcommand
## checkout 
versionid 可以恢复到指定版本 \
分支名称 可以切换到指定分支
## build
构造镜像
## pull
拉取
## push
## tag
docker tag source target
## logs
## info 
## inspect
显示 镜像相关信息 \
sudo docker inspect reg.dev.openpie.com/library/sig-storage/csi-node-driver-registrar:v2.5.0 --format='{{.Architecture}}' # 展示镜像支持的arch
# tool
## manifest
管理镜像清单，可以使用同一个镜像tag，管理不同架构的不同镜像。\
The **docker manifest** command has subcommands for managing image manifests and
manifest lists. A manifest list allows you to use one name to refer to the same image
built for multiple architectures.
### create 
创建一个本地清单，后续push到仓库。如下：\
```bash
docker manifest create your-harbor.com/your-project/your-image:latest \
    your-harbor.com/your-project/your-image:latest-amd64 \
    your-harbor.com/your-project/your-image:latest-arm64
```
### annotate
--arch 架构 \
--os  \
例子：
```bash
docker manifest annotate your-harbor.com/your-project/your-image:latest \
    your-harbor.com/your-project/your-image:latest-amd64 --arch amd64 --os linux
```
### push
将创建好的manifest上传到远程 eg
```bash 
docker manifest push your-harbor.com/your-project/your-image:latest
```
## compose
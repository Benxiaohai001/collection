# 概述
* 阿里巴巴开源混沌测试工具；
整体看上去像是注错工具；
# 编程语言
* go
# 适用范围
* 基础资源：比如 CPU、内存、网络、磁盘、进程等实验场景；
* Java 应用：比如数据库、缓存、消息、JVM 本身、微服务等，还可以指定任意类方法注入各种复杂的实验场景；
* C++ 应用：比如指定任意方法或某行代码注入延迟、变量和返回值篡改等实验场景；
* Docker 容器：比如杀容器、容器内 CPU、内存、网络、磁盘、进程等实验场景；
* 云原生平台：比如 Kubernetes 平台节点上 CPU、内存、网络、磁盘、进程实验场景，Pod 网络和 Pod 本身实验场景如杀 Pod，容器的实验场景如上述的 Docker 容器实验场景；
* 单机环境

# 故障

./blade c mem load 提高内存使用量
./blade c mem load --mem-percent 60
./blade c cpu fullload 提高cpu消耗
# 官方使用文档
[blade](https://chaosblade-io.gitbook.io/chaosblade-help-zh-cn/)
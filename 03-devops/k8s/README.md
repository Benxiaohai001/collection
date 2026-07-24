# k8s

## 知识大纲

### 1. 基础概念
- Cluster
- Node
- Pod
- Container
- Namespace
- Label / Annotation

### 2. 核心对象
- Pod
- Deployment
- ReplicaSet
- StatefulSet
- DaemonSet
- Job / CronJob
- Service
- Ingress

### 3. 控制面原理
- apiserver
- etcd
- scheduler
- controller-manager
- kubelet
- kube-proxy

### 4. 网络与存储
- Pod 网络
- Service 转发
- DNS
- Ingress / Gateway
- PV / PVC / StorageClass

### 5. 调度与运维
- requests / limits
- 探针
- 滚动更新
- HPA
- 日志与事件
- 故障排查

### 6. 安全
- RBAC
- [ServiceAccount](./6-安全/6.2-ServiceAccount.md)
- Secret
- NetworkPolicy

### 7. 实战场景
- 部署无状态服务
- 部署有状态服务
- 配置热更新
- 定时任务
- 灰度发布与回滚

### 8. 命令速查
- kubectl get
- kubectl describe
- kubectl logs
- kubectl exec
- kubectl rollout

## 记录方式
- 每篇笔记尽量围绕一个对象或一个问题展开。
- 统一写清楚：作用、关键字段、示例、常见坑、排查命令。
- 原理类内容放在“怎么工作”，实战类内容放在“怎么用”。
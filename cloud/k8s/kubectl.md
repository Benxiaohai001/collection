# patch
通过策略合并补丁、json合并补丁、或者json补丁更新资源的字段。
接受json和yaml格式。
# 设置默认命名空间
kubectl config set-context --current --namespace=your_namespace
# 进入pod的指定容器
kubectl exec -it -n jenkins postgres-pr-pr-92-68-59x1h-2jhb8-gctfd -c oracle -- bash
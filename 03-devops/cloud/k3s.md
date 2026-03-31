# 安装
参考： https://docs.k3s.io/zh/installation/configuration
```sh 
curl -sfL https://get.k3s.io | K3S_TOKEN=12345 sh -s - server --flannel-backend none
``` 
# 配置网络
参考：https://docs.tigera.io/calico/latest/getting-started/kubernetes/k3s/quickstart
```sh 
# 施工队
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.31.4/manifests/operator-crds.yaml
# 施工标准
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.31.4/manifests/tigera-operator.yaml
# 施工图纸
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.31.4/manifests/custom-resources.yaml
```
# 安装helm
```bash 
$ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
$ chmod 700 get_helm.sh
$ ./get_helm.sh
```
# rancher 
参考：https://ranchermanager.docs.rancher.com/zh/getting-started/quick-start-guides/deploy-rancher-manager/helm-cli
```bash 
helm repo add rancher-latest https://releases.rancher.com/server-charts/latest

kubectl create namespace cattle-system

kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/<VERSION>/cert-manager.crds.yaml

helm repo add jetstack https://charts.jetstack.io

helm repo update

helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace

# Windows Powershell
helm install cert-manager jetstack/cert-manager `
  --namespace cert-manager `
  --create-namespace
helm install rancher rancher-latest/rancher \
  --namespace cattle-system \
  --set hostname=<IP_OF_LINUX_NODE>.sslip.io \
  --set replicas=1 \
  --set bootstrapPassword=<PASSWORD_FOR_RANCHER_ADMIN>

# Windows Powershell
helm install rancher rancher-latest/rancher `
  --namespace cattle-system `
  --set hostname=<IP_OF_LINUX_NODE>.sslip.io `
  --set replicas=1 `
  --set bootstrapPassword=<PASSWORD_FOR_RANCHER_ADMIN>

```
# 集群中清理rancher agent
ns cattle-system cattle-fleet-system cattle-local-user-passwords cattle-impersonation-system
# 1. 删除所有的 Deployment 和 DaemonSet
kubectl -n cattle-impersonation-system delete deploy,ds --all

# 2. 删除所有的 Service 和 Secret
kubectl -n cattle-impersonation-system delete svc,secret --all

# 3. 专门针对 Rancher 的特有资源 (App/Chart)
kubectl -n cattle-impersonation-system delete apps.projectcalico.org --all 2>/dev/null
kubectl -n cattle-impersonation-system delete charts.helm.cattle.io --all 2>/dev/null

# 删除全局角色绑定（这些通常是权限锁死的原因）
kubectl get clusterrolebinding -o name | grep cattle | xargs kubectl delete
kubectl get clusterrole -o name | grep cattle | xargs kubectl delete

# 删除 Webhook（这是最容易导致后续安装失败的“地雷”）
kubectl delete mutatingwebhookconfigurations rancher.cattle.io
kubectl delete validatingwebhookconfigurations rancher.cattle.io

kubectl delete ns cattle-system cattle-fleet-system cattle-impersonation-system cattle-local-user-passwords

package main

import (
	"fmt"
	"os"
	"path/filepath"

	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/tools/clientcmd"
)

func main() {
	// 1. 实事求是：找到你电脑上的 K8s 配置文件（通常在 ~/.kube/config）
	home, _ := os.UserHomeDir()
	kubeconfig := filepath.Join(home, ".kube", "config")

	// 2. 建立因果：加载配置，告诉 Go 怎么连 K8s
	config, err := clientcmd.BuildConfigFromFlags("", kubeconfig)
	if err != nil {
		fmt.Printf("加载配置失败（是不是没装K8s或没配config？）: %v\n", err)
		return
	}

	// 3. 实例化：创建一个 K8s 的“客户端”客户端（就像你的数据库连接池）
	clientset, err := kubernetes.NewForConfig(config)
	if err != nil {
		fmt.Printf("创建客户端失败: %v\n", err)
		return
	}

	// 4. 核心动作：调取版本信息（这就是你要的“神”之视角）
	version, err := clientset.Discovery().ServerVersion()
	if err != nil {
		fmt.Printf("获取版本失败: %v\n", err)
		return
	}

	// 5. 结果呈现：看到这个，你的代码焦虑就杀掉了一半
	fmt.Printf("🎉 成功连接！当前 K8s 集群版本是: %s\n", version.GitVersion)
}

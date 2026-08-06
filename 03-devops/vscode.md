# 常用插件

## GitLens
显示代码历史提交记录的

## Remote-SSH
连接远程服务

### 跳转机配置

通过跳板机 B 访问目标机器 C（本地 A -> B -> C）

#### 方法一：ProxyJump 配置

编辑 `~/.ssh/config`：

```ssh
Host jump-server
    HostName <B服务器IP>
    User <用户名>
    Port 22

Host target-server
    HostName <C服务器IP>
    User <用户名>
    Port 22
    ProxyJump jump-server
```

#### 方法二：ProxyCommand 配置

```ssh
Host jump-server
    HostName <B服务器IP>
    User <用户名>

Host target-server
    HostName <C服务器IP>
    User <用户名>
    ProxyCommand ssh -W %h:%p jump-server
```

#### 方法三：SSH Config 穿透多层

A -> B -> C -> D 多层跳转：

```ssh
Host jump-b
    HostName <B服务器IP>
    User <用户名>

Host jump-c
    HostName <C服务器IP>
    User <用户名>
    ProxyJump jump-b

Host target-d
    HostName <D服务器IP>
    User <用户名>
    ProxyJump jump-c
```

#### 常用配置项

```ssh
Host *
    # 保持连接
    ServerAliveInterval 60
    ServerAliveCountMax 3
    
    # 转发 agent
    ForwardAgent yes
    
    # 端口转发
    LocalForward 8080 localhost:8080
```


## Groovy 相关
### Jenkins Extension Pack
### Groovy Lint, Format and Fix
跳转函数定义，远程情况下插件安装到远程机器。

## GitHub Copilot
写代码 AI 助手

---

## 手动下载插件
1. 通过 web 或其他方式下载安装包；
2. 将安装包复制到 `vscode/bin` 目录下面；
3. 执行安装命令：
   ```bash
   code --install-extension codelldb-x86_64-windows.vsix
   ```
   出现如下内容则证明安装成功：
   ```log
   Extension 'codelldb-x86_64-windows.vsix' was successfully installed.
   ```

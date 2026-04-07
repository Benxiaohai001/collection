# VSCode Remote SSH

## 跳转机配置

通过跳板机 B 访问目标机器 C（本地 A -> B -> C）

### 方法一：ProxyJump 配置

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

### 方法二：ProxyCommand 配置

```ssh
Host jump-server
    HostName <B服务器IP>
    User <用户名>

Host target-server
    HostName <C服务器IP>
    User <用户名>
    ProxyCommand ssh -W %h:%p jump-server
```

### 方法三：SSH Config 穿透多层

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

## 常用配置项

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

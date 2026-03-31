# 问题：
## grafana：origin not allowed
### 解决方案：
    * 配置文件中修改如下配置：
```bash 
[server]
# 这里两个域名应该改为浏览器访问的域名
domain = 
[security]
csrf_trusted_origins =
```

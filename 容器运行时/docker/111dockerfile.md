# ENTRYPOINT ["script.sh"] 与 ENTRYPOINT script.sh 区别
## ENTRYPOINT ["script.sh"] 是 JSON 数组格式，表示将 script.sh 作为可执行文件运行。
## ENTRYPOINT script.sh 是 Shell 格式，表示在容器启动时执行 script.sh 脚本。
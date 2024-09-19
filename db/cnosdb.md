
检查内存消耗：
MALLOC_CONF=prof:true


curl -H "authorization: xxx" 'http://127.0.0.1:8902/debug/jeprof'
调用这个接口会产生一个文件 /tmp/mem_profile.out

./jeprof --svg ./cnosdb ./mem_profile.out > ./mon_profile.svg

需要安装这工具 ： graphviz
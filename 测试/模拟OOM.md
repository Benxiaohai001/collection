<!-- 模拟系统OOM测试 -->
# linux：
## strss 
stress --vm 10 --vm-bytes 25G --vm-keep
```
stress 会对系统施加某些指定类型的压力；
使用： stress 【option】
--vm  启动几个分配/释放内存的worker
--vm-bytes 每个worker分配的内存大小；
 --vm-keep 一直占用内存，不释放
```
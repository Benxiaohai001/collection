# add
add alisa url ：添加远程仓库及别名；
# branch 检查分支，
-a 显示当前所有分支；\
-d [分支名称] 删除分支； \
# checkout
git checkout src/client.rs 修改该文件后，可以通过该命令恢复； \
git checkout log_id 恢复仓库代码到指定版本 \
git checkout . 恢复到当前目录最近一次提交的状态 \
# commit
# fetch:从远程获取代码库
# log
# rebase
# rev-parse 用于区分xxx list
git rev-parse HEAD 获取当前的commit id \
git rev-parse --short HEAD 获取当前短 id
# pull
git pull origin LTS/2.3:LTS/2.3 # 拉取远程分支，在本地新增一个分支
# push
git push --delete 分支名称  删除远程分支 \
git push 远程仓库名称   \
# remote：远程仓库
# reset
git reset --hard 版本库地址
# show: 查看提交记录
# submodule:  初始化 更新 检查子模块；
# TIP
## 从其他仓库拉取代码，新建分支：
git remote add yanyun_repo https://github.com/bartliu827/cnosdb.git
git fetch yanyun_repo
git checkout async_watch_v2
git push gitlab async_watch_v2:async_watch_v2

## 合并多个commit
git add . \
git commit -m "123" \
git rebase -i HEAD~2 \

git stash \
编辑删除第二次的提交信息 \
把这些 commit 合并 \
 
git push -f \
# reflog 查找引用历史

# 原理
内容寻址的文件系统
版本控制的用户界面
# 拉取远程指定分支到本地指定分支并切换
git checkout -b 本地分支名 origin/远程分支名
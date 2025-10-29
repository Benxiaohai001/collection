# add
add alisa url ：添加远程仓库及别名；
# branch 检查分支，
-a 显示当前所有分支；\
-d [分支名称] 删除分支； \
# cherry-pick
将某个commit 增加到某个分支 \
git cherry-pick commit-id
# checkout
git checkout src/client.rs 修改该文件后，可以通过该命令恢复； \
git checkout log_id 恢复仓库代码到指定版本 \
git checkout . 恢复到当前目录最近一次提交的状态 \
# clone 
克隆代码仓库到本地
-b branchname 指定仓库分支 \
--depth n 指定克隆几个commit \
--recurse-submodules 递归克隆子模块 \
`git clone -b main --depth 1 http:xxx.git` # 克隆主分支最新的commit \
# commit
# diff
展示不同commit 之间的不同
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
# 删除历史中某个commit
## 1. 启动交互式变基（例如删除最近5个提交中的中间提交）
git rebase -i HEAD~5

## 2. 在编辑器中标记要删除的 commit，将 `pick` 改为 `drop`
## 示例：
pick abc123 Commit A
drop def456 Commit B  # 删除此提交
pick ghi789 Commit C

## 3. 保存退出，解决可能的冲突
git add .
git rebase --continue

## 4. 强制推送更新后的历史
git push origin 分支名 --force

# 拉取远程分支到本地，并直接切换到该分支
git checkout -b tmp origin/tmp
## 分支代码不是最新的
该方法拉取的可能不是最新的commit，之前本地出现过同名分支可能会基于缓存创建新分支，可以在执行之前git fetch origin刷新远程分支信息

# 同步公司外部仓库代码
1. 公司内仓库创建一个空仓（不要添加任何内容）；
2. 克隆一个裸仓库到本地机器。
```git
git clone --mirror https://github.com/username/your-repo.git
cd your-repo.git
```
--mirror参数会克隆仓库的​​所有分支、标签和引用​​，为完整镜像做准备。
3. 将克隆仓库推送到公司内部新仓库。
```git
git push --mirror https://your-company-git-server/username/new-repo.git
```
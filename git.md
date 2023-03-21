# add
add alisa url ：添加远程仓库及别名；
# commit
# fetch:从远程获取代码库
# log
# rebase
# pull
# push
# remote：远程仓库
# reset
git reset --hard 版本库地址
# show: 查看提交记录
# submodule:  初始化 更新 检查子模块；
# 从其他仓库拉取代码，新建分支：
git remote add yanyun_repo https://github.com/bartliu827/cnosdb.git
git fetch yanyun_repo
git checkout async_watch_v2
git push gitlab async_watch_v2:async_watch_v2
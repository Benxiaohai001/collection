多版本管理
curl https://pyenv.run | bash
```.bashrc
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```
source ~/.bashrc
```pyenv
# 查看可安装的版本列表
pyenv install --list

# 安装特定版本，如 Python 3.9.7
pyenv install 3.9.7

# 查看已安装的版本
pyenv versions

# 设置全局默认版本
pyenv global 3.9.7

# 为特定项目目录设置局部版本（在该目录下执行）
pyenv local 3.8.12
```
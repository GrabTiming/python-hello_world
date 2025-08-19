
# 项目依赖管理

## 创建虚拟环境
```shell
python3 -m venv .venv
```
后面的.venv是环境名
## 激活虚拟环境
```shell
source .venv/bin/activate
```

## requirement.txt
这个文件用于标识项目中用到的依赖，可以通过下面命令生成requirement.txt
```shell
pip freeze > requirement.txt
```

然后分享给别人搭建项目的时候就可以直接执行命令一键安装所有依赖
```shell
pip install -r requirement.txt
```
然后requirement.txt有个缺点，当删除一个依赖A，它的那些间接依赖并不会被删除，而是保留了下来，所以需要用到pyproject.toml来解决这个问题。
## pyproject.toml
pyproject.toml直接添加依赖即可，删掉依赖也一样直接在dependencies操作

```
```toml
[project]
name = "pyproject-study"
version = "0.1.0"
description = "pyproject.toml study"
dependencies = [
    'Flask==2.0.1'
]
```

安装依赖的时候,添加-e参数，目的是不把源代码安装到python环境
```shell
pip install -e .venv 
```

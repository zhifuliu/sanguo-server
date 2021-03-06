# server

## 部署

1.  确保系统中已安装Nginx, uWSGI, Redis, Mongodb, swig

2.  安装依赖
    
    ```
    apt-get install build-essential
    apt-get install python-dev libmysqld-dev libncurses5-dev
    apt-get install python-pip
    apt-get install python-virtualenv
    apt-get install libpcre3-dev
    apt-get install libpcre++-dev
    ```

3.  Python虚拟环境。 在项目根目录中执行：

    ```
    virtualenv env
    source activate_env
    pip install -r requirements.txt

    如果速度太慢 可以用v2ex的镜像源： pip install -r requirements.txt -i http://pypi.v2ex.com/simple
    Mysql-python 可能会报 distribute 的错误，可以在 安装 requirements 之前先升级 distribute
    pip install -U distribute
    ```

4.  编译动态链接库

    ```
    ./compile-dll.sh
    ```

5.  **如果是直接部署到生产服务器，则略过此步，开发时需要执行这一步**

    ```
    获取最新的proto文件，并编译
    git submodule init
    git submodule update
    git submodule foreach git pull
    ./compile-protobufs.sh
    ```


6.  编辑配置文件，并启动程序

    ```
    cd sanguo
    cp config.template.xml config.xml
    vim config.xml

    start server
    正式服务器用 uWSGI 启动
    ```


## Mysql配置

*   [设置utf8编码][1]
*   TODO 增大cache


[1]: http://stackoverflow.com/questions/3513773/change-mysql-default-character-set-to-utf8-in-my-cnf


# 注意

## uWSGI 报错

ubuntu x64 系统上 uWSGI 可能会报这样的错误

`libgcc_s.so.1 must be installed for pthread_cancel to work`

解决办法:

**不要** 用pip 安装 uwsgi

下载安装包，修改 `uwsgiconfig.py` 文件，将对应的位置修改为：

```
1460     add_cflags = ['-lpthread', '-lgcc_s']
1461     add_ldflags = ['-lpthread', '-lgcc_s']
```


# 系统设置

## /etc/sysctl.cof

添加

```
net.core.somaxconn = 32768
net.ipv4.tcp_max_syn_backlog = 65536
net.core.netdev_max_backlog = 32768
```
然后执行 sudo sysctl -p


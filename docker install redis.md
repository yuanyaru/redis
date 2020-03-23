## 本示例共创建6个 redis 容器，3主3从
### 从 docker 库获取 redis 镜像
``` bash
docker pull redis
```
### 创建 redis 容器
创建6个容器，3主3从。接下来先为这6个容器创建6个不同的目录、端口和配置文件。
1. 在 /home/yyr 目录下创建 redis-cluster-test 文件夹
``` bash
mkdir -p /home/yyr/redis-cluster-test
cd  /home/yyr/redis-cluster-test
cat > redis-cluster.conf <<EOF
port ${PORT}
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
EOF
```
2. 在 /home/yyr/redis-cluster-test 目录下生成conf和data目录，并生成配置文件
``` bash
for port in `seq 6380 6385`; do
    mkdir -p ./${port}/conf && PORT=${port} envsubst < ./redis-cluster.conf > ./${port}/conf/redis.conf && mkdir -p ./${port}/data;
done
```
3. tree命令查看目录
``` bash
yum -y install tree
tree
```
4. 创建6个redis容器
``` bash
for port in `seq 6380 6385`; do 
     docker run --net=host --name=redis-${port} -v `pwd`/${port}/conf/redis.conf:/usr/local/etc/redis/redis.conf -d redis:latest redis-server /usr/local/etc/redis/redis.conf; 
done
```
### redis-trib.rb 启动主从集群
1. 如果没有ruby，请执行以下命令安装
``` bash
yum -y install ruby
```
* 由于CentOS7 yum库中ruby的版本支持到 2.0.0，但是gem安装redis需要最低是2.3.0，所以执行以下脚本采用rvm来更新ruby
``` bash
./rvm_update_ruby.sh
gem install redis
```
2. 将当前目录下 redis-trib.rb 拷贝至 /usr/local/bin
``` bash
cd /home/yyr/redis-cluster-test/
cp redis-trib.rb /usr/local/bin
```
3. 启动集群
``` bash
redis-trib.rb create --replicas 1 127.0.0.1:6380 127.0.0.1:6381 127.0.0.1:6382 127.0.0.1:6383 127.0.0.1:6384 127.0.0.1:6385
```
* 终端提示：Can I set the above configuration? (type 'yes' to accept): yes时，输入 yes
* 创建完成后提示：[OK] All 16384 slots covered.
### Redis客户端测试
``` bash
# 集群方式
docker exec -it redis-6380 redis-cli -c -p 6380
# 非集群方式
docker exec -it redis-6380 redis-cli -p 6380
```
### 问题
1. 偶而会出现集群启动失败
[root@nodeb3 yyr]# redis-trib.rb create --replicas 1 127.0.0.1:6380 127.0.0.1:6381 127.0.0.1:6382 127.0.0.1:6383 127.0.0.1:6384 127.0.0.1:6385
>>> Creating cluster
[ERR] Sorry, can't connect to node 127.0.0.1:6380
解决方法：
手动启动所有容器，再建立集群关系

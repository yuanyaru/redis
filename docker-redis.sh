#!/usr/bin/bash

docker pull redis

mkdir -p /home/yyr/redis-cluster-test
cd  /home/yyr/redis-cluster-test
cat > redis-cluster.conf <<EOF
port ${PORT}
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
EOF

for port in `seq 6380 6385`; do
    mkdir -p ./${port}/conf && PORT=${port} envsubst < ./redis-cluster.conf > ./${port}/conf/redis.conf && mkdir -p ./${port}/data;
done

yum -y install tree
tree

# 创建6个redis容器
for port in `seq 6380 6385`; do 
     docker run --net=host --name=redis-${port} -v `pwd`/${port}/conf/redis.conf:/usr/local/etc/redis/redis.conf -d redis:latest redis-server /usr/local/etc/redis/redis.conf; 
done

rvm_update_ruby.sh
gem install redis

cp redis-trib.rb /usr/local/bin
redis-trib.rb create --replicas 1 127.0.0.1:6380 127.0.0.1:6381 127.0.0.1:6382 127.0.0.1:6383 127.0.0.1:6384 127.0.0.1:6385
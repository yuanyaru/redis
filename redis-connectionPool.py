#!/usr/bin/python
# -*- encoding:utf-8 -*-

import redis

# redis 连接池
"""
redis-py 使用 connection pool 来管理对一个 redis server 的所有连接，避免每次建立、释放连接的开销。
默认，每个 Redis 实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数 Redis，
这样就可以实现多个 Redis 实例共享一个连接池。
"""
pool = redis.ConnectionPool(host="192.168.100.64", port=6379, db=1, max_connections=10)
r = redis.Redis(connection_pool=pool)
r.set('你好', 'redis 你好！')
x = r.get('你好')
print(str(x, encoding='utf-8'))
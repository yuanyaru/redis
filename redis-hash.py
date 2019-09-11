#!/usr/bin/python
# -*- encoding:utf-8 -*-

import redis

# redis string 操作
# 连接
r = redis.Redis(host="192.168.100.64", port=6379)

# hset(name, key, value) name 对应的 hash 中设置一个键值对（不存在，则创建；否则，修改）
r.hset('score', '数学', '90')
# hget(name, key)
x = r.hget('score', '数学')
print(x)

# 批量设置键值对
r.hmset('score', {'数学': 99, '语文': 90, '英语': 100})
# 获取多个 key 的值
x = r.hmget('score', ['语文', '数学'])
print(x)
# 获取 name 对应 hash 的所有键值
hgetall = r.hgetall('score')
print("r.hgetall('score'):", hgetall)

# 获取 name 对应的 hash 中键值对的个数
hlen = r.hlen('score')
print("r.hlen('score'):", hlen)

# 获取 name 对应的 hash 中所有的 key 的值
hkeys = r.hkeys('score')
print("r.hkeys('score'):", hkeys)

# 获取 name 对应的 hash 中所有的 value 的值
hvals = r.hvals('score')
print("r.hvals('score'):", hvals)

# 检查 name 对应的 hash 是否存在当前传入的 key
hexists = r.hexists('score', '数学')
print("r.hexists('score', '数学'):", hexists)

# 将 name 对应的 hash 中指定 key 的键值对删除
r.hdel('score', '语文', '英语')
hdel = r.hmget('score', ['语文', '数学', '英语'])
print(hdel)














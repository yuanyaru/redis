#!/usr/bin/python
# -*- encoding:utf-8 -*-
# redis hash 操作

import redis

# 连接
r = redis.Redis(host="192.168.100.64", port=6379)

# name 对应的 hash 中设置一个键值对（不存在，则创建；否则，修改）
r.hset('score', '数学', '90')
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

# 自增 name 对应的 hash 中的指定 key 的值，不存在则创建 key=amount
r.hincrby("当前值", 'num1', 1)
num1 = r.hget("当前值", 'num1')
print(num1)

r.hincrbyfloat("当前值", 'num2', 0.1)
num2 = r.hget("当前值", 'num2')
print(num2)

# 增量式迭代获取，对于数据大的数据非常有用，hscan 可以实现分片的获取数据，并非一次性将数据全部获取完，从而放置内存被撑爆
r.hmset('xxx', {'k1': 1, 'k2': 2, 'k3': 3, 'xx': 12345})
cursor1, data1 = r.hscan('xxx', cursor=0, match='k*', count=1)
cursor2, data2 = r.hscan('xxx', cursor=cursor1, match='k*', count=1)
print(cursor1, data1)
print(cursor2, data2)

# 利用 yield 封装 hscan 创建生成器，实现分批去 redis 中获取数据
r.hmset('xxxx', {'k1': 1, 'x1': 'x1', 'k2': 2, 'k3': 3, 'x2': 'x2'})
for item in r.hscan_iter('xxxx', match='k*', count=2):
    print(item)












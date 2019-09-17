#!/usr/bin/python
# -*- encoding:utf-8 -*-
# redis list 操作: redis 中的 List 在在内存中按照一个 name 对应一个 List 来存储

import redis

# 连接
r = redis.Redis(host="192.168.100.64", port=6379, db=1)

# 在 name 对应的 list 中添加元素-多个，每个新的元素都添加到列表的最左边
# rpush(name, values) 表示从右向左操作
r.lpush("queue", 1, 2, 3)

# 在 name 对应的 list 中添加元素-单个，只有 name 已经存在时，值添加到列表的最左边
# rpushx(name, value) 表示从右向左操作
r.lpushx("queue", "x")

# 在 name 对应的列表的某一个值前或后插入一个新值
r.linsert("queue", 'BEFORE', 'x', 'y')  # 在 queue 列表中‘x’值前插入‘y’

# 对 name 对应的 list 中的某一个索引位置重新赋值
r.lset("queue", 0, "helllo")
r.lset("queue", -1, "who")  # 给 queue 的最后一个值重新赋值为‘who’

x = r.llen("queue")
print(x)








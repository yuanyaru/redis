#!/usr/bin/python
# -*- encoding:utf-8 -*-
# redis list 操作: redis 中的 List 在在内存中按照一个 name 对应一个 List 来存储

import redis

# 连接
r = redis.Redis(host="192.168.100.64", port=6379, db=1)
# #########################################增操作###########################################

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

# #########################################删操作###########################################
# 先在列表中插入一些数据
r.lpush('list1', 1, 1, 2, 3, 4, 5)
r.lpush('list2', 1, 1, 2, 3, 4, 5)
print('list1 的长度为：%s, list2 的长度为：%s' % (r.llen('list1'), r.llen('list2')))
# r.lrem(name, num, value) : 在name对应的list中删除指定的值
# num=0，删除列表中所有的指定值；num=2,从前到后，删除2个；num=-2,从后向前，删除2个
r.lrem('list1', 0, 1)

# rpop(name) 表示从右向左操作
r.lpop('list1')  # 删除左侧第一个元素
r.ltrim('list1', 0, 1)  # 删除 list 中索引值不在 0-1 之间的数据

# r.brpop(keys, timeout)，从右向左获取数
# 循环删除列表‘list1’的数据，如果都被删除了，则开始删除列表‘list2’中的数据，直到循环结束
for i in range(5):
    r.blpop(('list1', 'list2'), 1)

# 打印列表的长度
print('list1的长度为:%s，list2的长度为:%s，' % (r.llen('list1'), r.llen('list2')))

# #########################################其他操作###########################################
strList = r.rpush('strList', 'a', 'b', 'c')
numList = r.rpush('numList', 1, 2, 3)

str = r.lrange('strList', 0, 1)  # 获取 strList 中0~1间的值
print(str)

# 从一个列表移除最右边的元素，同时将其添加至另一个列表的最左边
r.rpoplpush('strList', 'numList')
# 从一个列表的右侧移除一个元素并将其添加到另一个列表的左侧
# timeout，当 src 对应的列表中没有数据时，阻塞等待其有数据的超时时间（秒），0 表示永远阻塞
r.brpoplpush('strList', 'numList', 0)
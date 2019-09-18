#!/usr/bin/python
# -*- encoding:utf-8 -*-
# redis set 操作: Set 集合就是不允许重复的列表

import redis

# 连接
r = redis.Redis(host="192.168.100.64", port=6379, db=1)

# name 对应的集合中添加元素
r.sadd('set1', 1, 2, 3, '汉字')
r.sadd('set2', 1, 'a', 'b')

# 获取 name 对应的集合中元素个数
num = r.scard('set1')
print('set1 中元素的个数： %d' % num)

# 在第一个 name 对应的集合中且不在其他 name 对应的集合的元素集合
x1 = r.sdiff('set1', 'set2')
for i in x1:
    print('x1: ' + str(i, encoding='utf-8'))

# 获取第一个 name 对应的集合中且不在其他 name 对应的集合，再将其新加入到 dest 对应的集合中
r.sinterstore('newset', 'set1', 'set2')

# 检查 value 是否是 name 对应的集合的成员
x2 = r.sismember('set1', 1)
print(x2)

# 获取 name 对应的集合的所有成员
x3 = r.smembers('set1')
for i in x3:
    print('x3:' + str(i, encoding="utf-8"))

# 将某个成员从一个集合中移动到另外一个集合
r.smove('set1', 'set2', 0)

# 从集合的右侧（尾部）移除一个成员，并将其返回
x4 = r.spop('set1')
print('set1中移除的成员是；%s' % x4)

# 从 name 对应的集合中随机获取 numbers 个元素
x5 = r.srandmember('set1', 3)
for i in x5:
    print('x5:' + str(i, encoding="utf-8"))

# 在 name 对应的集合中删除某些值
r.srem('set1', 1, 2)

# 获取多一个name对应的集合的并集
x6 = r.sunion('set1', 'set2')
for i in x6:
    print('x6: %s' % str(i, encoding="utf-8"))

# 获取多一个name对应的集合的并集，并将结果保存到dest对应的集合中
r.sunionstore('set3', 'set1', 'set2')

# sscan(name, cursor=0, match=None, count=None)
# sscan_iter(name, match=None, count=None)
# 同字符串的操作，用于增量迭代分批获取元素，避免内存消耗太大
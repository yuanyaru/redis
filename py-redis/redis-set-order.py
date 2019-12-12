#!/usr/bin/python
# -*- encoding:utf-8 -*-
# redis set 操作: 有序集合，在集合的基础上，为每元素排序；元素的排序需要根据另外一个值来进行比较，
# 所以，对于有序集合，每一个元素有两个值，即：值和分数，分数专门用来做排序。

import redis

# 连接
r = redis.Redis(host="192.168.100.64", port=6379, db=1)

# 在 name 对应的有序集合中添加元素
r.zadd('score', {'语文': 55, '数学': 60, '英语': 70})
r.zadd('age', {'张三': 30, '李四': 30, '王五': 30, '赵六': 30, '语文': 30})
x1 = r.zcard('score')
print('s1对应集合的元素的数量是 %d' % x1)

# 获取 name 对应的有序集合中分数 在 [min,max] 之间的个数
x2 = r.zcount('score', 50, 60)
print('s2对应集合中分数在 [50,60] 之间的个数是：%d' % x2)

# 为有序集合 name 的成员 value 的 score 加上增量 amount
r.zincrby('score', 30, '语文')

# 按照索引范围获取 name 对应的有序集合的元素
# r.zrange(name, start, end, desc=False, withscores=False, score_cast_func=float)
x3 = r.zrange('score', 0, 2, desc=True, withscores=True, score_cast_func=float)
for i in x3:
    print(x3)
# 从小到大排序
# zrevrange(name, start, end, withscores=False, score_cast_func=float)

# 按照分数范围获取 name 对应的有序集合的元素
# zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)
x4 = r.zrangebyscore('score', 60, 90, start=0, num=2, withscores=True, score_cast_func=float)
for i in x4:
    print(i)
# 从大到小排序
# zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=float)

# 获取某个值在 name 对应的有序集合中的排行（从 0 开始）
x5 = r.zrank('score', '语文')
print("语文的分数在集合中的排行是：%d" % x5)
# zrevrank(name, value)，从大到小排序

# zrangebylex(name, min, max, start=None, num=None)
# 当所有成员都具有相同的分值时，会根据成员的值来进行排序，而这个命令则可以返回给定的有序集合键 key 中，元素的值介于 min 和 max 之间的成员
# 对集合中的每个成员进行逐个字节的对比，按照从低到高的顺序，返回排序后的集合成员。
# 两个字符串有一部分内容相同，命令会认为较长比较短大
# ZADD myzset 0 aa 0 ba 0 ca 0 da 0 ea 0 fa 0 ga
# r.zrangebylex('myzset', "-", "[ca") 结果为：['aa', 'ba', 'ca']
# 从大到小排序
# zrevrangebylex(name, max, min, start=None, num=None)

# 删除 name 对应的有序集合中值是 values 的成员
r.zrem('score', "数学")

# 根据排行范围删除
r.zremrangebyscore('age', 0, 2)

# 根据分数范围删除
x6 = r.zremrangebyscore('score', 30, 55)
print("删除个数是x6 = %d" % x6)

# 获取 name 对应有序集合中 value 对应的分数
x7 = r.zscore('score', '语文')
print("语文的分数是：%d" % x7)

# 获取两个有序集合的交集，如果遇到相同值不同分数，则按照aggregate进行操作
# aggregate的值为:  SUM  MIN  MAX
r.zinterstore('inter', ['score', 'age'], aggregate='SUM')  # 交集保存在集合 inter 中

# 获取两个有序集合的并集，如果遇到相同值不同分数，则按照aggregate进行操作
r.zunionstore('outer', ['score', 'age'], aggregate='SUM')  # 并集保存在集合outer中

# zscan(name, cursor=0, match=None, count=None, score_cast_func=float)
# zscan_iter(name, match=None, count=None, score_cast_func=float)
# 同redis-hash中的scan操作相似，相较于字符串新增score_cast_func，用来对分数进行操作
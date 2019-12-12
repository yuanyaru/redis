#!/usr/bin/python
# -*- encoding:utf-8 -*-
# redis string 操作

import redis
import time

# 连接
r = redis.Redis(host="192.168.100.64", port=6379)
"""
set(name, value, ex=None, px=None, nx=False, xx=False)
 在 Redis 中设置值，默认，不存在则创建，存在则修改
 参数：
 ex，过期时间（秒）
 px，过期时间（毫秒）
 nx，如果设置为 True，则只有 name 不存在时，当前 set 操作才执行
 xx，如果设置为 True，则只有 name 存在时，岗前 set 操作才执行
"""
r.set("name1", "张三", ex=10, nx=True)
x1 = r.get('name1')
print(str(x1, encoding='utf-8'))

# 只有 name 不存在时，执行设置操作（添加）
r.set('name1', '张三', ex=5)
r.setnx('name1', '李四')  # name1 存在，不执行
r.setnx('name2', '王五')  # name2 不存在，执行
x2 = r.get('name1')
x3 = r.get('name2')
print(str(x2, encoding='utf-8'))
print(str(x3, encoding='utf-8'))

# 设置值,可设置过期时间
# r.setex('name3', '李四', 3)
# time.sleep(3)
# x4 = r.get('name3')
# print(str(x4, encoding='utf-8'))

# r.set('name4', '张三')
# r.psetex('name4', 3, '李四')
# time.sleep(0.001)
# x5 = r.get('name4')
# print(str(x5, encoding='utf-8'))

"""
批量设置值 mset(*args, **kwargs)
如：
    mset(k1='v1', k2='v2') 或 mget({'k1': 'v1', 'k2': 'v2'})
    get(name) 获取值

批量获取 mget(keys, *args)
如：
    mget('ylr', 'Lily') 或 r.mget(['ylr', 'Lily'])
"""
r.mset({'name5': 'lisi', 'name6': '王五'})
x6 = r.get('name5')
x7 = r.mget('name5', 'name6')
x8 = r.mget(['name5', 'name6'])
print(x6, x7, x8)
print(str(x7[0]), str(x7[1], encoding='utf-8'))
print(str(x8[0]), str(x8[1], encoding='utf-8'))

# 设置新值并获取原来的值
r.set('name1', 'old')
x = r.getset('name1', 'new')  # 获取原来的值
y = r.get('name1')  # 获取新值
print(x, y)

# 获取子序列（根据字节获取，非字符） 如： "张三" ，0-3表示 "张" （一个汉字三个字节）
r.set('name1', '张三')
r.set('name2', 'lucky')
x = r.getrange('name1', 0, 2)
y = r.getrange('name2', 0, 2)
print(x, y)
print(str(x, encoding='utf-8'))

# 修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
r.set('name1', '张三')
r.set('name2', 'lucky')
r.setrange('name1', 3, '无忌')
r.setrange('name2', 1, 'hello')
x = r.get('name1')
y = r.get('name2')
print(x, y)
print(str(x, encoding='utf-8'))

# 返回 name 对应值的字节长度
r.mset({'name1': '里斯', 'name2': '张三'})
x = r.strlen('name1')
print(x)

# incr(self, name, amount=1) 自增 name 对应的值，当 name 不存在时，则创建 name＝amount，否则，则自增。
r.incr('y1', 2)
y1 = r.get('y1')
print(y1)

r.incrbyfloat('y2', 1.1)
y2 = r.get('y2')
print(y2)

# 自减
r.decr('y3', 1)
y3 = r.get('y3')
print(y3)

# 在 redis name 对应的值后面追加内容
r.set('x1', 'hello')
r.append('x1', ',world')
x = r.get('x1')
print(x)
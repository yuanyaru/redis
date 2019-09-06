#!/usr/bin/python
# -*- encoding:utf-8 -*-

import redis
import time

# redis string 操作
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

r.set('name1', '张三', ex=10, nx=True)
x1 = r.get('name1')
print str(x1).decode('utf-8')
"""
"""
setnx(name, value)
设置值，只有 name 不存在时，执行设置操作（添加）

r.set('name1', '张三', ex=5)
r.setnx('name1', '李四')  # name1 存在，不执行，name1 中值仍然是‘张三’
r.setnx('name2', '王五')  # name2 不存在，执行，name2 中值是‘王五’
x2 = r.get('name1')
x3 = r.get('name2')
print str(x2).decode('utf-8')
print str(x3).decode('utf-8')
"""
"""
setex(name, value, time)
设置值,可设置过期时间
参数：
    time，过期时间（数字秒 或 timedelta 对象）

r.setex('name3', '李四', 2)
time.sleep(3)
x = r.get('name3')
print str(x).decode('utf-8')
"""
"""
psetex(name, time_ms, value)
设置值
参数：
    time_ms，过期时间（数字毫秒 或 timedelta 对象）

r.set('name4', '张三')
r.psetex('name4', 3, '李四')
time.sleep(0.001)
x = r.get('name4')
print str(x).decode('utf-8')
"""
"""
批量设置值 mset(*args, **kwargs)
如：
    mset(k1='v1', k2='v2') 或 mget({'k1': 'v1', 'k2': 'v2'})
    get(name) 获取值

批量获取 mget(keys, *args)
如：
    mget('ylr', 'Lily') 或 r.mget(['ylr', 'Lily'])

r.mset({'name1': 'lisi', 'name2': '王五'})
x = r.get('name1')
x1 = r.mget('name1', 'name2')
x2 = r.mget(['name1', 'name2'])
print x, x1, x2
print str(x1[0]), str(x1[1]).decode('utf-8')
print str(x2[0]), str(x2[1]).decode('utf-8')
"""
"""
设置新值并获取原来的值
getset(name, value)

r.set('name1', 'old')
x = r.getset('name1', 'new')  # 获取原来的值
y = r.get('name1')  # 获取新值
print x
print y
"""
"""
getrange(key, start, end)
获取子序列（根据字节获取，非字符）
参数：
  name，Redis 的 name
  start，起始位置（字节）
  end，结束位置（字节）
如： "张三" ，0-3表示 "张"

r.set('name1', '张三')
r.set('name2', 'lucky')
x = r.getrange('name1', 0, 2)
y = r.getrange('name2', 0, 2)
print(x, y)
print(str(x, encoding='utf-8'))
"""
"""
setrange(name, offset, value)
修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
参数：
    offset，字符串的索引，字节（一个汉字三个字节）
    value，要设置的值

r.set('name1', '张三')
r.set('name2', 'lucky')
r.setrange('name1', 3, '无忌')
r.setrange('name2', 1, 'hello')
x = r.get('name1')
y = r.get('name2')
print(x, y)
print(str(x, encoding='utf-8'))
"""
# 返回name对应值的字节长度（一个汉字3个字节）
r.mset({'name1': '里斯', 'name2': '张三'})
x = r.strlen('name1')
print(x)

"""
incr(self, name, amount=1)
自增 name 对应的值，当 name 不存在时，则创建 name＝amount，否则，则自增。
参数：
    name,Redis的name
    amount,自增数（必须是整数）
"""
r.incr('x1', 2)
x1 = r.get('x1')
print(x1)

r.incrbyfloat('x2', 1.1)
x2 = r.get('x2')
print(x2)

# 自减
r.decr('x3', 1)
x3 = r.get('x3')
print(x3)

"""
append(key, value)
 在 redis name 对应的值后面追加内容
参数：
    key, redis的name
    value, 要追加的字符串
"""
r.set('x1', 'hello')
r.append('x1', ',world')
x = r.get('x1')
print(x)

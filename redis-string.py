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
"""
r.set('name1', 'old')
x = r.getset('name1', 'new')  # 获取原来的值
y = r.get('name1')  # 获取新值
print x
print y

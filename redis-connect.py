#!/usr/bin/python
# -*- encoding:utf-8 -*-

import redis

# redis 连接
r = redis.Redis(host="192.168.100.64", port=6379)
r.set('hello', 'world')
x = r.get('hello')
print(x)
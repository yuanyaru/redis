#!/usr/bin/python
# -*- encoding:utf-8 -*-

import redis

"""
redis-py 默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，
如果想要在一次请求中指定多个命令，则可以使用 pipline 实现一次请求指定多个命令，并且默认情况下一次 pipline 是原子性操作。
默认的情况下，管道里执行的命令可以保证执行的原子性，将transaction设置为False,可以禁用这一特性。
"""
pool = redis.ConnectionPool(host='192.168.100.64', port=6379, db=1)
r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)

pipe.set('name', '原雅茹')
pipe.set('age', '20')

pipe.execute()

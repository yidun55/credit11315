#!usr/bin/env python
#coding: utf-8

import redis
r = redis.Redis(host="localhost", port=6379)

f = open("credit11315/proxy_ips.txt", "r")

for i in f:
    r.zadd("credit11315_proxy_ips:sorted_set", i.strip(), 1)

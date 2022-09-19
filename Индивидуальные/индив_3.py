# !/usr/bin/env python3
# -*- coding: utf-8 -*-

for i in range(100, 1000):
    a = i % 10
    b = i // 10 % 10
    c = i // 100
    if (a + b + c) % 7 == 0 and i % 7 == 0:

        print(i)
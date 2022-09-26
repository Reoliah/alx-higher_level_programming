#!/usr/bin/python3
a = 89
b = 10
c, d = a, b
a, b = d, c
print("a= {:d} - b= {:d}".format(a,b))

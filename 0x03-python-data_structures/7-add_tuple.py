#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuplesum = ()
    tup1 = tuple_a + (0, 0)
    tup2 = tuple_b + (0, 0)
    tuplesum = tup1[0] + tup2[0], tup1[1] + tup2[1]
    return tuplesum

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # fill with 0 if necessary
    fill_a = tuple_a[:2] + (0, 0)[:2 - len(tuple_a)]
    fill_b = tuple_b[:2] + (0, 0)[:2 - len(tuple_b)]
    sum_1 = fill_a[0] + fill_b[0]
    sum_2 = fill_a[1] + fill_b[1]
    return (sum_1, sum_2)

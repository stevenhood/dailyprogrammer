#!/usr/bin/env python

# [2015-06-08] Challenge #218 [Easy] Making numbers palindromic
# http://bit.ly/1C4nMf9

from collections import defaultdict

def reverse_digits(x):
    return int(str(x)[::-1])

def is_palindrome(s):
    if type(s) != str:
        s = str(s)
    return s == s[::-1]

def calc(origin):
    val = origin
    steps = 0
    while not is_palindrome(val) and steps < 10000:
        val += reverse_digits(val)
        steps += 1
    if is_palindrome(val):
        print('%d gets palindromic after %d steps: %d' % (origin, steps, val))
        return val
    return None

calc(123)
calc(286)
calc(196196871)

palins = defaultdict(list)
for n in range(1001):
    key = calc(n)
    palins[key].append(n)

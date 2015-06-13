#!/usr/bin/env python

# [2015-06-01] Challenge #217 [Easy] Lumberjack Pile Problem
# http://bit.ly/1IQyCgs

import sys

def print_grid(grid, n):
    """ Prints an n by n grid """
    for i in range(0, n*n, n):
        print(*piles[i:i + n])

def solve(grid, to_place):
    while to_place > 0:
        smallest = min(piles)
        for i in range(len(piles)):
            if piles[i] == smallest:
                piles[i] += 1
                to_place -= 1
                if to_place == 0:
                    break;
    return grid

if len(sys.argv) < 2:
    print('Usage: lumberjack_pile.py <input file>')
    sys.exit(1)
path = str(sys.argv[1])
n, to_place, *piles = [int(n) for n in open(path).read().split()]

print('n =', n)
print('to_place =', to_place)
print('Grid:')
print_grid(piles, n)

piles = solve(piles, to_place)

print('Solution:')
print_grid(piles, n)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_combs(comb=[]):
    if len(comb) == 0:
        for x1 in range(0, 3):
            comb.append(x1)
            get_combs(comb)
            comb.pop(-1)
    elif len(comb) == 1:
        for x3 in range(0, 4):
            comb.append(x3)
            get_combs(comb)
            comb.pop(-1)
    elif len(comb) == 2:
        for x5 in range(0, 5):
            comb.append(x5)
            get_combs(comb)
            comb.pop(-1)
    elif len(comb) == 3:
        for x7 in range(0, 6):
            comb.append(x7)
            get_combs(comb)
            comb.pop(-1)
    elif len(comb) == 4:
        for x2 in range(2, 41 - sum(comb)):
            comb.append(x2)
            get_combs(comb)
            comb.pop(-1)
    elif len(comb) == 5:
        for x4 in range(3, 41 - sum(comb)):
            comb.append(x4)
            get_combs(comb)
            comb.pop(-1)
    elif len(comb) == 6:
        for x6 in range(4, 41 - sum(comb)):
            comb.append(x6)
            get_combs(comb)
            comb.pop(-1)
    elif len(comb) == 7 and sum(comb) == 40:
        combs.append(comb[:])


combs = []
get_combs()

f = open('combs.txt', 'w')
f.write('x1 x2 x3 x4 x5 x6 x7\n')
for comb in combs:
    for x in comb:
        if 0 <= x <= 9:
            f.write(str(x) + '  ')
        else:
            f.write(str(x) + ' ')
    f.write('\n')
f.close()

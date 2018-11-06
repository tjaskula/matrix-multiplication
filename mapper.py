#! /usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    id_mat, row, col, val = line.split(",")

    if id_mat == "A":
        for x in range(1, 3):
            print '%s %s %s %s' % (row, x, col, val)
    else:
        for y in range(1, 3):
            print '%s %s %s %s' % (y, col, row, val)


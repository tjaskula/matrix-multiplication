#! /usr/bin/env python
import sys

# number of rows in A
m = int(sys.argv[1])

# number of columns in B
p = int(sys.argv[2])

for line in sys.stdin:
    line = line.strip()
    id_mat, row, col, val = line.split(",")

    if id_mat == "A":
        for x in range(p):
            print '%d %d %d %f' % (int(row), int(x), int(col), float(val))
    else:
        for x in range(m):
            print '%d %d %d %f' % (int(x), int(col), int(row), float(val))


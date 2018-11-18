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
            print '%s %s %s %s' % (row, x, col, val)
    else:
        for x in range(m):
            print '%s %s %s %s' % (x, col, row, val)


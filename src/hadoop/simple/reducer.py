#! /usr/bin/env python

import sys

current_key = None
current_j = None
current_val = 0
result = 0

for line in sys.stdin:
    sub_key1, sub_key2, j, val = line.strip().split()
    key = '%s-%s' % (sub_key1, sub_key2)

    try:
        val = int(val)
    except ValueError:
        continue
    if (current_key == key) and (current_j == j):
        result += current_val * val
    else:
        if current_key != key:
            if current_key:
                print(current_key, result)
            current_key = key
            result = 0

        current_j = j
        current_val = val

print(current_key, result)

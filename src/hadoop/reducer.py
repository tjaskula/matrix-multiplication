#! /usr/bin/env python

import sys

cle = None
j = None
current_cle = None
current_j = None
current_v = 0
produit = 0
somme = 0

for line in sys.stdin:
    sub_cle1, sub_cle2, j, val = line.strip().split()
    cle = '%s-%s' % (sub_cle1, sub_cle2)

    try:
        val = int(val)
    except ValueError:
        continue
    if (current_cle == cle) and (current_j == j):
        produit = current_v * val
    else:
        if (current_cle == cle) and (current_j != j):
            somme += produit
            current_j = j
            current_v = val
        else:
            if current_cle:
                print(current_cle, somme + produit)
            current_cle = cle
            current_j = j
            current_v = val
            somme = 0
            produit = 0

if (current_cle == cle) and (current_j == j):
    print(current_cle, somme + produit)

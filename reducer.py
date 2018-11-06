#!usr/bin/env/python

import sys
current_cle=None
current_j=None
current_v=0
produit=0
somme=0

for line in sys.stdin:
	line=line.strip()
	cle=line.split()[0:2]
	j= line.split()[2]
	v=line.split()[3]
	try:
		v=int(v)
	except ValueError:
		continue
	if (current_cle==cle) and (current_j==j): 
			produit=current_v*v
	else:
		if (current_cle==cle) and (current_j != j):
			somme+=produit
			current_j=j
			current_v=v

		else :
			if current_cle:
				print(current_cle,somme+produit)
			current_cle=cle
			current_j=j
			current_v=v
			somme=0
			produit=0
	
if (current_cle==cle) and (current_j==j):
	print(current_cle, somme+produit)
	

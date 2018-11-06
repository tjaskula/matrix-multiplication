#!usr/bin/env/python

import sys

for line in sys.stdin:
	line=line.strip()
	id_mat=line.split(",")[0]
	i=line.split(",")[1]
	j=line.split(",")[2]
	v=line.split(",")[3]
	if id_mat=="A":
		for x in range(1,3):
			print(int(i),int(x),j,v)
	else:
		for y in range(1,3):
			print(int(y),int(j),i,v)


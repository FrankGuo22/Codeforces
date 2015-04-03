# 82A.py
name = ['Sheldon','Leonard','Penny','Rajesh','Howard']
n = int(raw_input())
curound = 5
while n > curound:
	n -= curound
	curound *= 2
print name[int(5*n/(curound+1))]
# 263A.py
m,n = 0,0
for i in range(5):
	a = map(int,raw_input().split())
	for j in range(5):
		if a[j]!=0:
			m = i
			n = j
			break
print abs(m-2)+abs(n-2)
		
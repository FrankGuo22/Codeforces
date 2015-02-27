# 158A.py
 
a = map(int, raw_input().split())
b = map(int, raw_input().split())
sum = 0
for k in b:
	if (k >=b[a[1]-1]) and (k > 0):
		sum += 1
print sum
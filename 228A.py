# 228A.py
ans = 1
a = map(int,raw_input().split())
if a[1]!=a[0]:
	ans += 1
if a[2]!=a[0] and a[2]!=a[1]:
	ans += 1
if a[3]!=a[0] and a[3]!=a[1] and a[3]!=a[2]:
	ans += 1
print 4-ans
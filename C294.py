# C294.py
a = map (int, raw_input().split())
sum = 0
while a[0]!=a[1] and a[0]> 0 and a[1]> 0:
	if a[0]> a[1]:
		a[0] -= 2
		a[1] -= 1
		sum += 1
	else:
		a[0] -= 1
		a[1] -= 2
		sum += 1
if a[0] == a[1]:
	sum += (a[0]+a[1])/3
print sum 

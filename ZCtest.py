# coding =utf-8
import math
a = map(int,raw_input().split())
if a[1]/a[3] < a[2]/a[4]:
	large=2
	small=1
else:
	large=1
	small=2
max = 0
t = 0
for i in range(100000):
	if i * a[small+2]>a[0]:
		break
	if (int((a[0]-i*a[small+2])/a[large+2]))*a[large]+a[small]*i > max:
		max = (int((a[0]-i*a[small+2])/a[large+2]))*a[large]+a[small]*i
print max

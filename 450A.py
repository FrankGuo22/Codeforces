# coding =utf-8
n,m = map(int,raw_input().split())
a = map(int,raw_input().split())
exist=n

while exist!=1:
	for i in range(n):
		if a[i]==0:
			continue
		a[i]-=m
		if a[i]<=0:
			a[i]=0
			exist -= 1
		if exist==1:
			break
			
for i in range(n):
	if a[i]!=0:
		print i+1
		break
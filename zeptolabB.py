# coding = utf-8
t = int(input())
n = 1
for i in range(t):
	n *= 2
u = n
a = []
total = 0
a = map(int,raw_input().split())
sum = 0
i = u-2
while i>=0:
	if (i>=n-2):
		if a[i]>a[i+1]:
			sum +=a[i]-a[i+1]
			a[i+1]=a[i]
		else:
			sum +=a[i+1]-a[i]
			a[i]=a[i+1]
		if i==(u*2-4):
			u=u/2
			i=u-2
		else:
			i += 2
	else:
		if a[i]+a[2*i+2]>a[i+1]+a[2*i+4]:
			sum +=a[i]+a[2*i+2]-a[i+1]-a[2*i+4]
			a[i]=a[i+1]=a[i]+a[2*i+2]
		else:
			sum +=a[i+1]+a[2*i+4]-a[i]-a[2*i+2]
			a[i]=a[i+1]=a[i+1]+a[2*i+4]
		if i == 0:
			break
		if i==(u*2-4):
			u=u/2
			i=u-2
		else:
			i += 2
	
print sum
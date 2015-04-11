# coding =utf-8
n = int(input())
a = map(int,raw_input().split())
t = []
start, end = 0,0
for i in range(n-1):
	t.append(a[i+1]-a[i])
for i in range(n-1):
	if t[i]<0:
		start=i
		while i<n-1 and t[i]<0:
			t[i]=1
			i+= 1
		end = i
		if start!=0:
			t[start-1]=a[end]-a[start-1]
		if end !=n-1:
			t[end]=a[end+1]-a[start]
		break
	else:
		i+= 1
chk = True
for i in range(n-1):
	if t[i]<0:
		chk =False
if chk:
	print 'yes'
	print '{} {}'.format(start+1,end+1)
else:
	print 'no'
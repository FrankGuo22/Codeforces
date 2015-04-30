# coding =utf-8
I=lambda:map(int,raw_input().split())
n,m = I()
a = I()
l =[]
chk =[]
sum=0
for i in range(100004):
	chk.append(True)
for i in range(m):
	l.append(int(raw_input()))
q =[]
for i in range(n-1,-1,-1):
	if chk[a[i]]==True:
		chk[a[i]]=False
		q.append(sum+1)
		sum+= 1
	else:
		q.append(sum)
for i in range(m):
	print q[n-l[i]]
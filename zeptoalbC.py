# coding =utf-8
a = map(int,raw_input().split())
small = 1
large = 2
if a[3]>a[4]:
	small = 2
	large = 1
b=[]
for i in range(0,a[0]+1):
	if i<a[small+2]:
		b.append(0)
	if i<a[large+2] and i>=a[small+2]:
		b.append(b[i-a[small+2]]+a[small])
	if i>=large:
		if b[i-a[small+2]]+a[small]>b[i-a[large+2]]+a[large]:
			b.append(b[i-a[small+2]]+a[small])
		else:
			b.append(b[i-a[large+2]]+a[large])
print b[a[0]]


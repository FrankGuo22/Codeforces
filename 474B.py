# coding =utf-8
n = int(input())
a = map(int,raw_input().split())
m = int(input())
q = map(int,raw_input().split())
t = []
for i in range(a[0]):
	t.append(1)
for i in range(1,n):
	a[i]+=a[i-1]
	for j in range(a[i-1],a[i]):
		t.append(i+1)
for i in q:
	print t[i-1]

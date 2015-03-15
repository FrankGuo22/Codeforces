
n = int(raw_input())
a = map(int, raw_input().split())
b = {}
for i in range(101):
	b[i] = i
for i in range(1,n+1):
	b[a[i-1]]= i
for i in range(1,n+1):
	print b[i]
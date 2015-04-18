#coding = uft -8
I = lambda:map(int,raw_input().split())
n,t,c =I()
a = I()
ans = 0
forb = []
for i in range(n):
	if a[i]>t:
		forb.append(i)
forb.append(10000000)
j = 0
for i in range(n-c+1):
	if forb[j]<i:
		j+=1
	if forb[j]>=i and forb[j]<=i+c-1:
		continue
	else:
		ans +=1
print ans
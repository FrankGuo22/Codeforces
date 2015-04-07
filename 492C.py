# coding =utf-8
I = lambda:map(int,raw_input().split())
n,r,avg=I()
sum = n*avg
temp = []
for i in range(n):
	a,b=I()
	sum-=a
	temp+=[(b,r-a)]
temp.sort()
i,ans=0,0
while sum>0:
	a,b=temp[i]
	term = min(sum,b)
	sum -= term
	ans += term*a
	i += 1
print ans
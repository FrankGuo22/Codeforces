# coding =utf-8
n,l = map(int,raw_input().split())
a = sorted(map(int,raw_input().split()))
ans = max(a[0],l-a[n-1])
for i in range(1,n):
	ans=max(ans,(a[i]-a[i-1])/2.0)
print ans
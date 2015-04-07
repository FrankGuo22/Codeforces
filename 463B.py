# coding =utf-8
n = int(input())
a= map(int,raw_input().split())
ans,energy,i = a[0],0,0
while i<n-1:
	if a[i+1]<=a[i]:
		energy += a[i]-a[i+1]
		i += 1
	else:
		if energy>=a[i+1]-a[i]:
			energy = energy - (a[i+1]-a[i])
			i += 1
		else:
			t = a[i+1]-a[i]
			t -= energy
			energy = 0
			ans += t
			i += 1
print ans
	
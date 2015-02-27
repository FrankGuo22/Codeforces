#231A.py


ans=0
for _ in range(input()):
	a = map(int, raw_input().split())
	if a[0]+a[1]+a[2]>=2:
		ans+=1
print ans
# 379A.py

a = map(int,raw_input().split());
ans = 0;
recy = 0;
while a[0]!=0:
	ans += a[0];
	t = (a[0]+recy)/a[1];
	recy = recy+a[0]-t*a[1];
	a[0]=t;
print ans;
# 467A.py

n = int(raw_input())
ans = 0
for i in range(n):
	a = map(int,raw_input().split())
	if a[1]-a[0]>=2:
		ans += 1;
print ans;
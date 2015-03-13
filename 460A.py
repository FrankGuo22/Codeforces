# coding = utf-8

a = map(int,raw_input().split())
ans = 0
while (a[0]!=0):
	ans += 1
	a[0] -= 1
	if ans % a[1]==0:
		a[0] += 1
print ans
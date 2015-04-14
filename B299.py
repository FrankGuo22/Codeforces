# coding =utf-8
n = raw_input()
ans = 0
zhi = 1
for i in range(len(n)-1):
	zhi *=2
	ans  += zhi
ans += 1
zhi = 1
for i in range(len(n)-1,-1,-1):
	if n[i]=='7':
		ans += zhi
		zhi *=2
	else:
		zhi *=2
print ans
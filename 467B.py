# coding = utf-8
n,m,k = map(int,raw_input().split())
arn = []
def toBinary(n):
	return ''.join(str(1 & n >> i) for i in range(25)[::-1])
for i in range(m+1):
	arn.append(int(raw_input()))
st = toBinary(arn[m])
ans = 0
for i in range(m):
	po = toBinary(arn[i])
	diff = 0
	for j in range(25):
		if po[j]!=st[j]:
			diff += 1
	if diff<=k:
		ans += 1
print ans
	


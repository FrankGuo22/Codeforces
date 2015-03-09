# D294.py

a = map(int,raw_input().split())
ans = 0
string = raw_input()

for i in range(len(string)):
	sum[i] = a[int(string[i])-int('a')]
	sum[i] += sum[i-1]
	alb[int(string[i])-int('a')].append(i)

for i in range(26):
	for j in alb[i]:
		ans += mapp[sum[j-1]]
		mapp[sum[j]] += 1
	clear(mapp)

print mapp

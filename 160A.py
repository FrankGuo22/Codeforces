# 160A.py

n = raw_input()
a = map(int, raw_input().split())
a.sort(reverse = True);
sum = 0
for i in a:
	sum += i
sum /= 2
ans = 0
num = 0
for i in a:
	ans += i
	num += 1
	if ans > sum:
		print num
		break
		
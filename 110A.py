# 236A.py

a = raw_input()
ans = 0
for ch in a:
	if ch == '4' or ch =='7':
		ans += 1

if ans == 4 or ans == 7:
	print 'YES'
else:
	print 'NO'
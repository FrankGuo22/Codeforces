# 236A.py
a = raw_input()
num = []
ans = 0
for ch in a:
	if not ch in num:
		ans += 1;
		num.append(ch);
if ans % 2 == 0:
	print 'CHAT WITH HER!'
else:
	print 'IGNORE HIM!'
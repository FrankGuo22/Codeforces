# 96A.py

string =raw_input()
last = '2'
max = 1
for c in string:
	if c == last:
		now += 1
		if now > max:
			max = now 
	else:
		last = c
		now = 1
if max >= 7:
	print 'YES'
else:
	print 'NO'
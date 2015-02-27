# 133A.py

chk = 0 
string = raw_input()
for ch in string:
	if ch =='H' or ch=='Q' or ch =='9':
		chk = 1
		print 'YES'
		break
if chk == 0:
	print 'NO'
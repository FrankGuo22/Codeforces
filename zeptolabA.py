# coding = utf-8
n = input()
s = raw_input()
a = []
chk = 0
for i in range(len(s)):
	if s[i]=='*':
		a.append(i+1)
for i in a:
	for j in range(1,len(s)/4):
		if (i+j in a) and (i+2*j in a) and (i+3*j in a) and (i+4*j in a):
			chk = 1
			print 'yes'
			break
	if chk:
		break
if chk == 0:
	print 'no'
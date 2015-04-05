# coding = utf-8
n = int(input())
s = raw_input()
a = []
chk = 0
for i in range(n):
	if s[i]=='*':
		a.append(i+1)
for i in a:
	for j in range(1,n/2):
		if (i+j in a) and (i+2*j in a) and (i+3*j in a) and (i+4*j in a):
			chk = 1
			print 'yes'
			break
	if chk:
		break
if chk == 0:
	print 'no'
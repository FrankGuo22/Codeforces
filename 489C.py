# coding = utf-8
m,s = map(int,raw_input().split())
q =''
u = s 
for i in range(m):
	if s>=9:
		q += '9'
		s -= 9
	elif s !=0:
		q +=str(s)
		s = 0
	else: q += '0'
if u==0:
	 print '-1 -1'
else:
	t = q[::-1]
	if t[0]=='0':
		print q,q
	else:
		print t,q

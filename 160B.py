# coding = utf-8
a =[]
b =[]
n = raw_input()
s = raw_input()
for i in range(len(s)):
	if i<len(s)/2:
		a.append(int(s[i]))
	else:
		b.append(int(s[i]))
a.sort()
b.sort()
chk1,chk2 = True,True
for i in range(len(s)/2):
	if a[i]>b[i]:
		continue
	else:
		chk1=False
for i in range(len(s)/2):
	if a[i]<b[i]:
		continue
	else:
		chk2=False

if chk1 or chk2:
	print 'YES'
else:
	print 'NO'
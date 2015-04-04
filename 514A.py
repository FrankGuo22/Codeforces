# coding = utf-8
s = str(raw_input())
t = ''
p = 0
for i in s:
	if p == 0 and i =='9':
		t = t + i;
		p += 1
		continue
	p += 1
	if ord(i)>ord('4'):
		t = t+chr(9-(ord(i)-ord('0'))+ord('0'))
	else:
		t = t + i
print t
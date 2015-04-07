# coding =utf-8
n = int(input())
s = str(raw_input())
p =[]
for i in s:
	if i=='1':
		continue
	if i=='2':
		p.append(2)
	if i=='3':
		p.append(3)
	if i=='4':
		p.append(3)
		p.append(2)
		p.append(2)
	if i=='5':
		p.append(5)
	if i=='6':
		p.append(5)
		p.append(3)
	if i=='7':
		p.append(7)
	if i=='8':
		p.append(7)
		p.append(2)
		p.append(2)
		p.append(2)
	if i=='9':
		p.append(7)
		p.append(3)
		p.append(3)
		p.append(2)
p.sort(reverse=True)
stringnow =''
for i in p:
	stringnow = stringnow +str(i)
print stringnow
	
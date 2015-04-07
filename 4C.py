# coding =utf-8
strcol = {}
for i in range(int(raw_input())):
	strtemp = raw_input()
	v = strcol.get(strtemp,0)
	print [ 'OK',strtemp+str(v)][v>0]
	strcol[strtemp] = v + 1
# coding = utf - 8
n =raw_input()
q = 0 
if len(n)>=2:
	q=int(n[-2]+n[-1])
else:
	q = int(n)
if q % 4 ==0:
	print '4'
else:
	print '0'
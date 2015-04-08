# coding = utf -8
n = int(input())
a = map(int,raw_input().split())
s = ''
pos=0
while pos<n-1:
	if min(a[pos],a[pos+1])==a[pos]:
		for i in range(a[pos]-1):
			s += 'PRPL'
		if a[pos]==0:
			s +='R'
			pos += 1
		else:
			s +='PR'
			a[pos+1] = a[pos+1]-a[pos]+1
			a[pos]=0
			pos += 1
	else:
		for i in range(a[pos+1]):
			s += 'PRPL'
		for i in range(abs(a[pos+1]-a[pos])-1):
			s += 'PRL'
		if pos == n-2:
			s += 'P'
			pos += 2
		else:
			s += 'PRR'
			a[pos+1] = 0
			a[pos] = 0
			pos += 2
if pos == n-1 and a[pos]>0:
	for i in range(a[pos]-1):
		s += 'PLR'
	s += 'P' 
print s
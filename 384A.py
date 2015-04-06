# coding = utf-8
n =int(input())
s1 =''
s2 =''
if n%2==0:
	for i in range(n/2):
		s1 +='C.'
		s2 +='.C'
	print n*n/2
	for i in range(n/2):
		print s1
		print s2
else:
	for i in range(n/2):
		s1 +='C.'
		s2 +='.C'
	s1 +='C'
	s2 +='.'
	print (n*n+1)/2
	for i in range(n/2):
		print s1
		print s2
	print s1
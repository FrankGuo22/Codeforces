# coding = utf-8
I = lambda:map(int,raw_input().split())
a,b,n = I()
for i in range(n):
	l,t,m =I()
	if a+(l-1)*b>t:
		print '-1'
	else:
		left= l
		right = (t-a)/b+1
		while (left<=right):
			if (a+(l-1)*b+a+((right+left)/2-1)*b)*((right+left)/2-l+1)/2<=t*m:
				left =(left+right)/2+1
			else:
				right =(left+right)/2-1
		print left-1
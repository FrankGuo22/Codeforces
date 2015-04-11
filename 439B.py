# coding =utf-8
I = lambda:map(int,raw_input().split())
n,x = I()
a = sorted(I())
ans =0
for i in a:
	ans +=x*i
	if x==1:
		continue
	else:
		x-=1
print ans		
	

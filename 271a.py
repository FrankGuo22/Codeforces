# 271A.py
def distt(n):
	a[0]= n % 10;
	a[3]= n / 1000;
	a[2]= (n-a[3]*1000) / 100;
	a[1]= ((n-a[0])/10) % 10;
	if a[0]==a[1] or a[1]==a[2] or a[2]==a[3] or a[0]==a[2] or a[0]==a[3] or a[1]==a[3]:
		return False
	return True

a ={};
n = int(raw_input());
chk = False;
while chk==False:
	n += 1;
	chk = distt(n);
	
print n;
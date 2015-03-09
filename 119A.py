# 119A.py

def gcd(a,b):
	if b != 0:
		return gcd(b, a% b);
	else:
		return a;

a = map(int,raw_input().split())

while True:
	t = gcd(a[2],a[0]);
	if a[2] < t:
		print '1';
		break;
	a[2] -= t;
	t = gcd(a[2],a[1]);
	if a[2] < t:
		print '0';
		break;
	a[2] -= t;
	
	
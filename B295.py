# B295.py

att = map(int, raw_input().split())

n = att[0]
m = att[1]
ans = 0
while n != m:
	ans += 1
	if 2*n > m and n < m:
		if m % 2 == 0:
			ans += n-m/2
			n = m
		else:
			ans += n-(m+1)/2+1
			n = m
	if n > m:
		n -= 1
	elif 2*n <= m:
		n *= 2
			
print ans
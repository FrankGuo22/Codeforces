# 116A.py
# lala
capacity = 0
current = 0
for _ in range(input()):
	a = map(int, raw_input().split())
	current = current - a[0] + a[1]
	if current > capacity:
		capacity = current 
	
print capacity

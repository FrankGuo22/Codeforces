# 148A.py
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
d = int(raw_input())
ans = 0 
for i in range(int(raw_input())):
	if ((i+1) % a) == 0 or ((i+1) % b) == 0 or ((i+1) % c) == 0 or ((i+1) % d) ==0:
		ans += 1
print ans
# 266A.py

n = raw_input()
string = raw_input()
ans = 0
for i in range(1,len(string)):
	if string[i]==string[i-1]:
		ans += 1
print ans
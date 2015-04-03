# 266B.py
a = map(int,raw_input().split())
string = raw_input()

for i in range(a[1]):
	for j in range(len(string)-1):
		if string[j]=='B' and string[j+1]=='G':
			string[j+1] = "B"
			string[j] = "G"
print string
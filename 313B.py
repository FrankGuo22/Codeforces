# coding =utf-8
s = raw_input()
jud = []
jud.append(0)
nowis = 0
for t in range(len(s)-1):
	if s[t]==s[t+1]:
		jud.append(nowis+1)
		nowis += 1
	else:
		jud.append(nowis)
for i in range(int(input())):
	j,k=map(int,raw_input().split())
	print jud[k-1]-jud[j-1]
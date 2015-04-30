# coding = utf-8
n = int(raw_input())
s1 =raw_input()
s2 =raw_input()
ans = 0
for i in range(n):
	if abs(int(s1[i])-int(s2[i]))>5:
		ans +=(10-abs(int(s1[i])-int(s2[i])))
	else:
		ans +=abs(int(s1[i])-int(s2[i]))
print ans
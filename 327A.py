# coding = utf-8
n = input()
a = map(int,raw_input().split())
b = []
count = 0
for i in a:
	if i == 1:
		b.append(-1)
		count += 1
	else:
		b.append(1)
sum = 0
max = -2
for j in b:
	sum += j
	if sum>max:
		max = sum
	if sum < 0:
		sum = 0
print max+count
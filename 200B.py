# coding = utf - 8
n = raw_input()
a = map(int,raw_input().split())
sum = 0
for i in a:
	sum += i
f1,f2 = float(sum),float(n)
print '{0:.12f}'.format(f1/f2)
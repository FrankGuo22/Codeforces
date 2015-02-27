# 282A.py

ans = 0 
for _ in range(input()):
	string = raw_input();
	if string[0]=='+' or string[2]=='+':
		ans += 1
	else:
		ans -= 1
print ans
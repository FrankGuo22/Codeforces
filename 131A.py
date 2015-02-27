# 131A.py

string = raw_input()
check = 1
for ch in string[1:]:
	if ch.islower():
		print string
		check = 0
		break
if check == 1:
	if string[0].islower():
		print str(string[0].upper()) + str(string[1:].lower())
	else:
		print string.lower()


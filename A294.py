# A294.py
white = 0
black = 0
whitepart ={'Q':9,'R':5,'B':3,'N':3,'P':1,'K':0}
blackpart ={'q':9,'r':5,'b':3,'n':3,'p':1,'k':0}
for _ in range(8):
	string = raw_input()
	for ch in string:
		if ch != '.' and ch.islower():
			black += blackpart[ch]
		elif ch !='.' and ch.isupper():
			white += whitepart[ch]
if white > black:
	print 'White'
if white < black:
	print 'Black'
if white == black:
	print 'Draw'
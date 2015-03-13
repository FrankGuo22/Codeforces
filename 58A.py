# coding = utf-8
string = raw_input()
chk = False
for i in range(len(string)):
	if string[i] == 'h':
		for j in range(i+1,len(string)):
			if string[j]=='e':
				for k in range(j+1,len(string)):
					if string[k]=='l':
						for l in range(k+1,len(string)):
							if string[k]=='l':
								for m in range(l+1,len(string)):
									if string[m]=='o':
										chk = True
										
if chk== False:
	print 'NO'
else:
	print 'YES'
	
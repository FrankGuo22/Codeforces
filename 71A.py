#71A.py

for _ in range(input()):
    s= raw_input()
    print s[0]+str(len(s)-2)+s[-1] if len(s)>10 else s

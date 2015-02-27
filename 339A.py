# 339A.py

a = map(int, raw_input().split('+'))
a.sort()
print '+'.join([str(c) for c in a])
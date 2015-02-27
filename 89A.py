# 89A.py






str = raw_input().lower()
new = ".".join([c for c in str if not c in 'aoyeui'])

print "."+new

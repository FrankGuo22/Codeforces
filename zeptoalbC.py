C, Hr, Hb, Wr, Wb = map(int, raw_input().split())
ans = 0
for i in xrange(100000):
    if C/Wr < i: break
    ans = max(ans, i*Hr+(C-i*Wr)/Wb*Hb)
for i in xrange(100000):
    if C/Wb < i: break
    ans = max(ans, i*Hb+(C-i*Wb)/Wr*Hr)
print ans
# coding = utf-8
n=input();t=map(int,raw_input().split())
print max(sum(t[x::i])for i in range(1,n/3+1)if n%i<1 for x in range(i))
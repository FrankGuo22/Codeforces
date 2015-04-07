# coding =utf-8
n,m=map(int,raw_input().split())
print '{} {}'.format((n%m)*(n/m+1)*(n/m)/2+(m-n%m)*(n/m)*(n/m-1)/2 ,(n-m+1)*(n-m)/2)
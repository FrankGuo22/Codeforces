#coding =utf-8
s = int(raw_input())
t = ''
ten=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
single = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
if s<=19:
	print single[s]
else:
	if s %10==0:
		print ten[s/10-2]
	else:
		print str(ten[s/10-2])+'-'+str(single[s%10])
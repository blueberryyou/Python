sign=1
for x in range(1,101):
	sign = 1
	for i in range(2,int(x/2)):
		if x%i==0:
			sign=0;
	if sign==1:
		print(x,end='   ')
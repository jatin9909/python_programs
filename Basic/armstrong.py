def check(x):
	a=x
	len=int(0)
	while(int(a)!=0):
		a = a / 10
		len+=1

	sum=0;
	temp = x
	while(temp!=0) :
		r = temp%10
		sum=sum+pow(r,len)
		temp=temp//10

	print(sum)							

		
	return (sum==x)

n = int(input("Enter "))
print(check(n))
import array as arr

a = arr.array('i',[])
n  = int(input("Enter size"))

for i in range(n):
	x= int(input("Enter value"))
	a.append(x)


print(a)
sum=int(0)

for i in a:
	sum=sum+i

print(sum)	
print(sum(a))
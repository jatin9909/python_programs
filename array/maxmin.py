import array as arr

a = arr.array('i',[])
n  = int(input("Enter size"))

for i in range(n):
	x= int(input("Enter value"))
	a.append(x)

min=a[0]
max=a[n-1]

for i in a:
		if i>max:
				max=i

for i in a:
            if i<min:
                        min=i

print(max)
print(min)                        		
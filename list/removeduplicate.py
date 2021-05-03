a = [int(x) for x in input().split()]
b=[]

for i in a:
	if i not in b:
		b.append(i)

print(b)
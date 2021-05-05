a = [int(x) for x in input().split()]
start, end = [int(x) for x in input().split()]

temp=a[start:end]

temp.reverse()

for x in range(start,end):
	a[x]=temp[x-start]

print(a)	
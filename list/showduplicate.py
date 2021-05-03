def repeat(a):
	size = len(a)
	lst=[]
	for i in range(size):
		k=i+1
		for j in range(k,size):
			if a[i]==a[j] and a[i] not in lst:
				lst.append(a[i])
	return lst			

a = [int(x) for x in input().split()]

print(repeat(a))
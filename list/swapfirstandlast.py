def swap(a):
	n = len(a)
	temp = a[0]
	a[0] = a[n-1]
	a[n-1] = temp


a=[int(x) for x in input().split()]
print(a)

swap(a)
print(a)
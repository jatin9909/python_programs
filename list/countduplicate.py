def dup(a):
	result=dict((i, a.count(i)) for i in a)

	return result

a = [int(x) for x in input().split()]

print(dup(a))
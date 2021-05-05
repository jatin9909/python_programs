def sort_list(a,b):
	zip_list = zip(b,a)
	z = [x[1] for x in sorted(zip_list)]
	return z



a = input().split()
b = [int(x) for x in input().split()]

print(sort_list(a,b))
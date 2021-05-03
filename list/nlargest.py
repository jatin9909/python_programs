a = [int(x) for x in input().split()]

a.sort(reverse=True)
n = len(a)
print(a)

N = int(input("Enter upto where you want largest number"))

for x in (a[0],a[N-1]):
	print(x)
a = [int(x) for x in input().split()]

b = [int(x) for x in input("Enter the numbers you don't want in list").split()]

a = [ele for ele in a if ele not in b]

print(a)
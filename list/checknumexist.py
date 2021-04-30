a = [int(x) for x in input().split()]
n = int(input("Enter the number you want to find"))

check=0
for i in a:
	if i==n:
		print("yes")
		check=1
		break

if check==0:
		print("no")	
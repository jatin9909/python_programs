lst=[]
n = int(input("Enter size"))

for i in range(0,n):
	ele = int(input())
	lst.append(ele)

print(lst)	

temp=[]

for i in range(0,2):
	temp.append(lst[i])

print(temp)
d=0
for i in range(2,n):
	lst[d]=lst[i]
	d=d+1

lst[:]=lst[:d]+temp
print(lst)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list=[]
no_of_letters = int(input("enter How many letter you want"))
no_of_numbers = int(input("Enter how many numbers you want"))
no_of_symbols = int(input("Enter how many symbnols you want"))

for i in range(1, no_of_letters+1):
	password_list.append(random.choice(letters))

for i in range(1,no_of_numbers+1):
	password_list.append(random.choice(numbers))

for i in range(1,no_of_symbols+1):
	password_list.append(random.choice(symbols))

print(password_list)	
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
		password+=char

print(password)		

if len(password)>10:
	password=password[:10]

print(password)	
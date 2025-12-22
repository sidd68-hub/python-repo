import random


print("Welcome to password Generator!")


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9',]
symobols = ['!','@','#','$','%','^','&','*','(',')',]

passowrd_list = []
password = ''
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many number would you like?\n"))

for i in range(1,nr_letters + 1):
    passowrd_list.append(random.choice(letters))

for i in range(1, nr_symbols +1):
    passowrd_list.append(random.choice(symobols))

for i in range(1, nr_numbers):
    passowrd_list.append(random.choice(numbers))

random.shuffle(passowrd_list)
print(passowrd_list)

for i in passowrd_list:
    password += i
print(password)    


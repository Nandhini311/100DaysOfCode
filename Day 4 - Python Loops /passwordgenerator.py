password_list = []
for char in range(0,nr_letters+1):
    password_list.append(random.choice(letters))
for number in range(0, nr_symbols+1):
    password_list.append(random.choice(numbers))
for symbol in range(0, nr_numbers+1):
    password_list.append(random.choice(symbols))

'''now my list will have required items for the password, need to think about arranging them randomly'''
print(password_list)
random.shuffle(password_list)
print(password_list)
'''shuffles the original list in place'''

password = ""
for i in password_list:
    password += i

print(password)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your easy_password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# creating the letters for pw
pw_letters = ''
for letter in range(1, (nr_letters + 1)):
    pw_letters += random.choice(letters)

# creating the symbols for pw
pw_symbols = ''
for symbol in range(1, (nr_symbols + 1)):
    pw_symbols += random.choice(symbols)

# creaing the numbers for pw
pw_numbers = ''
for number in range(1, (nr_numbers + 1)):
    pw_numbers += random.choice(numbers)

# creating the easy_password (order not randomised)
easy_password = (pw_letters + pw_symbols + pw_numbers)

# converting easy_password to a list and shuffle
password_list = list(easy_password)
random.shuffle(password_list)

# creating the hard_password (order randomised)
hard_password = ""
for new in password_list:
    hard_password += new

# printing the password
print(f"Your password is: {hard_password}")

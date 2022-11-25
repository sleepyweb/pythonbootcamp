print("Welcome to Happy Lounge!")
id_proof = (input('''Do you have your Photo ID Card with you?
'''))
entry_fee = 0

# this is an example of how if and else works

# the first if statement is checking for the id_proof
if id_proof.lower == 'yes':
    print("You can enter the club :) ")
    age = int(input("What is your age? "))

    # this is an example of nested if statement
    if age < 10:
        entry_fee = 10
        print(f"Entry fee for children: ${entry_fee}")
    
    # this is an example elif statement
    elif age <= 18:
        entry_fee = 15
        print(f"Entry fee for teenagers: {entry_fee}")

    # using logical operator to check multiple condition in same if statement
    elif (age >= 30) and (age <= 40):
        entry_fee = 5
        print(f'''There is a special discount for age group of thirties 🎉.
Entry fee: {entry_fee}''')
    
    # this an example of nested else statement
    else:
        print(f"Entry fee for adults: {entry_fee}")

    card_member = input("Do you hold our membership card? Y or N. ")

    # this is an independent condition
    if card_member == "N":
        entry_fee += 5
   
    print(f"Your Entry Fee is ${entry_fee}")

# this is an else statement    
else:
    print("You can't enter the club :( ")
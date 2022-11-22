# greeting message
print("Welcome to the tip calculator!")

# taking user input for bill and tip
bill = int(input("What was the bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))

# calculating total bill
total_bill = bill + ((bill*tip)/100)

# taking user input for how many person
person = int(input("How many people to split the bill? "))

# calculating per person
per_person = total_bill / person

# printing the result
print(f"Each person should pay: {round(per_person, 2)}")

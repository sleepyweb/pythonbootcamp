for number in range(1, 101):

    # checking for divisible both by 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    # checking for divisible by 3
    elif number % 3 == 0:
        print("Fizz")
    
    # checking for divisible by 5
    elif number % 5 == 0:
        print("Buzz")

    # for other numbers
    else:
        print(number)

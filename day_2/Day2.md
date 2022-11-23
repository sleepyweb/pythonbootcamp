
![Day 2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/b69f3hd0nuam0q4mxsbt.jpg)

## Course Outline:
### Data Types: 

The day starts with data types. There are mainly 4 data types in Python.

- _string:_ string of characters
- _integer:_ whole numbers
- _float:_ floating point numbers
- _boolean:_ logic [ `TRUE`, `FALSE`]

big numbers like 1,000,000 can be writen as `1_000_000`, Python interpreter would recognize that.

### Type Error, checking and conversion:

To check the data types we can use `type()`

How to convert between data types?
```
num = "404" # it's a string

int_num = int(num) # it becomes an int
float_num = float(num) #it becomes a float
```

### Mathematica operations:

Python follows the PEMDAS rule.
- P: Parentheses
- E: Exponents
- M: Multiplication
- D: Division
- A: Addition
- S: Subtraction

### Number manipulation and f'strings

to round off any number, `round()` can be used.

f-strings are formatted strings.

```
value_pi = 3.141592653589793238
approx_value_pi = round(value_pi, 3) # this is how round off works

# this is how f-strings work
print(f"The approximated value of pi: {approx_value_pi}")
```

## Project: Tip Calculator
**Description:** A tip calculator which takes the bill value adds the tip and split it into how many folks are there.
**My Solution:** [tip_calculator.py](https://github.com/sleepyweb/pythonbootcamp/blob/main/day_2/tip_calculator.py)

[Some Relaxation Videos for Focus](https://youtu.be/JzxmO3Mi2io)


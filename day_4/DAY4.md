![Day 4](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cm5mz1pwj36axjesxcfk.jpg)

## Course Outline:

### Random Module:
`random` is a python module which generates [pseudo-random numbers](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators). 

What are Module? Modules are like code library.
To use a module we need to import it.
```
import random
```
### Lists:
Lists are data types which are used to store collection of data in single variable.
```
coffee_beans = ['Robusta', 'Arabica', 'Liberica', 'Excelsa', 'Bourb',
                'Catuai', 'Catimor', 'Jamaican Blue']

# this is how we access a list
# this is going to print 'Arabica' instead of 'Robusta'
# Python consider the first place of the list as 0
print(coffee_beans[1]) 

# to change a value in the list
coffee_beans[4] = 'Bourbon'

# to add a new value in the end of the list
coffee_beans.append('Geisha')
```

### IndexErrors and Nested Lists

If we try to access any value which is out of the list it throws `IndexError`.

Nested lists are multiple lists in one list.

```
# these are different lists
windows = ['Windows 11', 'Windows 10', 'Windows 8']
mac = ['Ventura', 'Monterey', 'Big Sur']
android = ['Tiramisu', 'Snow Cone', 'Red Velvet Cake']

# this is a nested list of the above 3 lists
os = [windows, mac, android]
```


## Project: Rock, Paper or Scissors Game
**Description:** It's a classic hand game originating from China, usually played between minimum 2 players.

**My Solution:** [rock_paper_scissors.py](https://github.com/sleepyweb/pythonbootcamp/blob/main/day_4/rock_paper_scissors.py)

[Cozy Study Room](https://youtu.be/5WwWvCITm6k)

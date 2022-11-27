
![Day 5](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kanutauw1wehc3hhindg.jpg)
## Course Outline:
### Loops:
`for` loop is used for iteration over a list(some other data structures)
```
sports = ["Basketball", "Tennis", "Baseball", "Volleyball"]

# this is a for loop
for sport in sports:

    # this will print each strings of the sports list indvidually
    print(sport)
```
Output:
```
Basketball
Tennis
Baseball
Volleyball
```
In two coding challeneges [avg_height.py](https://github.com/sleepyweb/pythonbootcamp/blob/main/day_5/avg_height.py) and [student_score.py](https://github.com/sleepyweb/pythonbootcamp/blob/main/day_5/student_score.py) we saw how with the `for` loop built-in functions like `sum`, `len` and `max` can be executable.

### for loops and the range() function
`range` function gives sequence of numbers. By default range function starts from 0 and 1 increments.
```
for number in range(5):
    print(number)
```

Output:
```
0
1
2
3
4
```
`range` function with multiple arguments
```
for number in range(5, 101, 10): # range(start, stop, step)
    print(number)
```
Output:
```
5
15
25
35
45
55
65
75
85
95
```
Today has been the a little difficult one so far using the for loop and range function. Learnt how some built-in function works. Used the random library on multiple exercises and got more familiar with `random.choice()` and `random.shuffle()`

## Project: Password Generator
**Description:** It generates a random password consisting letters, number, and symbols. 

**My Solution:** [password_generator.py](https://github.com/sleepyweb/pythonbootcamp/blob/main/day_5/password_generator.py)

[4 Hours of Ambient Study Music To Concentrate](https://youtu.be/4GnVDPD01as)

*P.S. It's fun to watch football while coding!*

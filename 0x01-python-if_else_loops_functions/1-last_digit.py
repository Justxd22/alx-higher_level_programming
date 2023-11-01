#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(str(number)[-1])
last = last * -1 if number < 0 else last
string = "greater than 5" if last > 5 else "less than 6 and not 0"
string = "0" if last == 0 else string
print(f"Last digit of {number} is {last} and is {string}")

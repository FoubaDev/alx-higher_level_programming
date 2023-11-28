#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
while number >= 0:
    last = number % 10
    if last > 6:
        print(f"Last digit of {number} is {last} and is greather than 5")
    elif last in range(1, 6):
        print(f"Last digit of {number} is {last} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {last}  and is 0")
    break
if number < 0:
    last = abs(number) % 10
    print(f"Last digit of {number} is {-last} and is less than 6 and not 0")

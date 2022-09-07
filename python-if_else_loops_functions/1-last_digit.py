#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = - digit
print(f"Last digit of {number} is {digit} and is ")
if digit > 5:
    print("great than 5")

elif digit < 5:
    print("less then 6 and not 0")
else:
    print("0")

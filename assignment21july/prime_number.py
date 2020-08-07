'''
 Program to check prime number
'''
from math import sqrt

number = int(input())
if number > 1:
    result = True
    for i in range(2, int(sqrt(number)) + 1): #  efficient way
        if number % i == 0:
            result = False
            break
    if result:
        print(number, ' is a prime number')
    else:
        print(number, ' is not a prime number')
else:
    print(number, ' is not a prime number')

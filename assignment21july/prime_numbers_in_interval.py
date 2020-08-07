# Program to check prime number in given range

from math import sqrt


def check_prime(number):
    if number > 1:
        result = True
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                result = False
                break
        return result
    else:
        return False


lower_limit = int(input('enter lower limit '))
upper_limit = int(input('enter upper limit '))
prime_numbers = []

for number in range(lower_limit, upper_limit):
    if check_prime(number):
        prime_numbers.append(number)
print(prime_numbers)

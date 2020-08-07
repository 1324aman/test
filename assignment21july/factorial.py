# Program to find factorial of a number

number = int(input())
factorial = 1

for i in range(2, number + 1):
    factorial *= i
print('factorial of {0} is {1} '.format(number, factorial))

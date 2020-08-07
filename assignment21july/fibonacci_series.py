#  Python Program to Print the Fibonacci sequence


def fibonacci(number):
    if number >= 0:
        if number == 1 or number == 0:
            return number
        else:
            return fibonacci(number - 1) + fibonacci(number - 2)
    else:
        return -1


number_of_terms = int(input('enter number of terms '))
fibonacci_series = []

for i in range(1, number_of_terms + 1):
    fibonacci_series.append(fibonacci(i))

print(fibonacci_series)

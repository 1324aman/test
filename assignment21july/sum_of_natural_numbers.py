# Python Program to Find the Sum of Natural Numbers

number_of_terms = int(input())
sum_of_numbers = 0

for i in range(1, number_of_terms + 1):
    sum_of_numbers += i
print('sum of', number_of_terms, 'natural number is', sum_of_numbers)

'''2. Write a function that reverses a string.

Input: "Hello
Output: "olleH

Note: Write all possible solutions, mention which solution is best and why.
'''

# Slicing method

string = input()
print(string[::-1])

# Appending from last character to first in new input_string

input_string = input()
length = len(input_string)-1
revesed_string = ''

while(length >= 0):
    revesed_string += input_string[length]
    length -= 1
print(revesed_string)

# Using reversed method which returns an iterator

string = input()
string = reversed(string)  # It returns an iterator
reversed_string = ''
for char in string:
    reversed_string += char
print(reversed_string)

# Converting string to list and then applying reverse method

string = input()
list_of_chars = list(string)
list_of_chars.reverse()
reversed_string = ''.join(list_of_chars)
print(reversed_string)

# using recursion


def reverse_string(input_string):
    if(len(input_string) == 1):
        return input_string
    else:
        return reverse_string(input_string[1:]) + input_string[0]


print(reverse_string('hello world'))

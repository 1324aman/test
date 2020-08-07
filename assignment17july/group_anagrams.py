'''
. Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:

[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

'''

input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
dictionary = {}

for item in input_list:
    string = ''.join(sorted(item))
    if string in dictionary:
        dictionary[string].append(item)
    else:
        dictionary[string] = []
        dictionary[string].append(item)
result = []

for value in dictionary.values():
    result.append(value)

result.sort(key=len, reverse=True)
print(result)

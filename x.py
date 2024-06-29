# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:51:18 2024

@author: khush
"""

#occurance of each vovel

def count_vowel_occurrences(string):
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for char in string:
        if char.lower() == 'a':
            vowel_counts['a'] += 1
        elif char.lower() == 'e':
            vowel_counts['e'] += 1
        elif char.lower() == 'i':
            vowel_counts['i'] += 1
        elif char.lower() == 'o':
            vowel_counts['o'] += 1
        elif char.lower() == 'u':
            vowel_counts['u'] += 1
    return vowel_counts

# Example usage:
string = input("Enter a string: ")
occurrences = count_vowel_occurrences(string)
print("Occurrences of each vowel:")
for vowel, count in occurrences.items():
    print(vowel, ":", count)

"""

Enter a string: khushi
Occurrences of each vowel:
a : 0
e : 0
i : 1
o : 0
u : 1

"""
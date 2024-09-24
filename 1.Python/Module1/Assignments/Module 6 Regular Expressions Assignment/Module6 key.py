# Module 6 key Regular Expressions Assignment

### 1) Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)	

import re
def is_allowed_specific_char(string):
	charRe = re.compile(r'[^a-zA-Z0-9]')
	string = charRe.search(string)
	return not bool(string)
 
print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))

### 2) Write a Python program to replace all occurrences of space, comma, or dot with a colon.


def replace_with_colon(input_str):
    for char in [' ', ',', '.']:
        input_str = input_str.replace(char, ':')
    return input_str

# Example usage:
input_str = "Hello, world. How are you today?"
new_str = replace_with_colon(input_str)
print(new_str)




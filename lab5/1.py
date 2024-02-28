#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

word = "AabAbbbbabbbba"

print(re.findall("ab*", word))
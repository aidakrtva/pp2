#Write a Python program to split a string at uppercase letters.

import re

text = """ Jojo's Bizarre Adventure" is_like a rollercoaster of_absurdity on steroids. Picture flamboyant characters_posing dramatically while summoning Stand powers – it's like a fashion_show meets a superhero_showdown. Created by the genius Hirohiko Araki, this anime is so extra that even the laws of physics take a backseat to its sheer fabulousness."""

pattern = re.compile("(?=[A-Z])")

text_rows = pattern.split(text)

print(text_rows)
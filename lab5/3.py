#Write a Python program to find sequences of lowercase letters joined with a underscore
import re

text = """Jojo's Bizarre Adventure" is_like a rollercoaster of_absurdity on steroids. Picture flamboyant characters_posing dramatically while summoning Stand powers – it's like a fashion_show meets a superhero_showdown. Created by the genius Hirohiko Araki, this anime is so extra that even the laws of physics take a backseat to its sheer fabulousness."""

print (re.findall ("[a-z]+_[a-z]+", text))
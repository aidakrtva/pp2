#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re 

text = """Jojo's Bizarre Adventure" is_like a rollercoaster of_absurdity on steroids. Picture flamboyant characters_posing dramatically while summoning Stand powers – it's like a fashion_show meets a superhero_showdown. Created by the genius Hirohiko Araki, this anime is so extra that even the laws of physics take a backseat to its sheer fabulousness."""

print (re.findall( "[A-Z][a-z]", text))
print (re.findall( "[A-Z][a-z]+", text))

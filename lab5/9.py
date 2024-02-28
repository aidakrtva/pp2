#Write a Python program to insert spaces between words starting with capital letters.

import re

text = """Jojo'sBizarreAdventure" is_like a rollercoaster of_absurdity on steroids. PictureFlamboyant characters_posing dramatically while summoning Stand powers – it's like a fashion_show meets a superhero_showdown. Created by the genius Hirohiko Araki, this anime is so extra that even the laws of physics take a backseat to its sheer fabulousness."""

def func(text):
    pattern = r"([a-z])([A-Z])"
    replaced_text = re.sub(pattern, r"\1 \2", text)
    return replaced_text


res = func(text)
print(res)
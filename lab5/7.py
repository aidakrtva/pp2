#Write a python program to convert snake case string to camel case string.

import re

text = """Jojo's Bizarre Adventure" is_like a rollercoaster of_absurdity on steroids. Picture flamboyant characters_posing dramatically while summoning Stand powers – it's like a fashion_show meets a superhero_showdown. Created by the genius Hirohiko Araki, this anime is so extra that even the laws of physics take a backseat to its sheer fabulousness."""

pattern = re.findall ("[a-z]+_[a-z]+", text)



def tostr(pattern, text):
    res= ' '.join(pattern)
    return res


def func(snake_case):
    words = snake_case.split('_')
    camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    camel_case = ''.join(camel_case_words)
    return camel_case

list_to_string = tostr(pattern,text)

camel_case_output = func(list_to_string)

print( camel_case_output)

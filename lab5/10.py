#Write a Python program to convert a given camel case string to snake case.
import re 


text = """Jojo's Bizarre Adventure" isLike a rollercoaster ofAbsurdity on steroids. Picture flamboyant characters_posing dramatically while summoning Stand powers – it's like a fashionShow meets a superheroShowdown. Created by the genius Hirohiko Araki, this anime is so extra that even the laws of physics take a backseat to its sheer fabulousness."""

pattern = re.findall ("[a-z]+[A-Z]+[a-z]+", text)

def tostr(pattern, text):
    res= ' '.join(pattern)
    return res


def func(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper() and snake_case:
            snake_case += '_'
        snake_case += char.lower()
    return snake_case

list_to_string = tostr(pattern,text)
snake_case_output = func(list_to_string)
print( snake_case_output)
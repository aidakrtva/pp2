#Write a Python program to write a list to a file.
with open('5.txt', 'w') as file:
    lst = ["Hi", 'my', 'bd', [6, 8 , 2005], "now im", {18}]
    file.write(' '.join(map(str, lst)))
    
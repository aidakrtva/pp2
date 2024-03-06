#Write a Python program to copy the contents of a file to another file
import os

with open("7.txt", "x") as file: # "x" is used to create a file
    pass

with open('4.txt', 'r') as file:
    with open('7.txt', 'w') as file2:
        file2.write(file.read())
        # for i in file: file2.write(i)
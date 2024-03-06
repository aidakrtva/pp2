#Write a Python program to count the number of lines in a text file.
import os

path = '/Users/aida/Documents/pp2-aida/githowto/repositories/work/lab6/dir_and_files/4.txt'

with open(path, 'r') as file:
    whatodo = file.readlines()
    
    print(len(whatodo))
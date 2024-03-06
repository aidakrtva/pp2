#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os 
from time import sleep

path = '/Users/aida/Documents/pp2-aida/githowto/repositories/work/lab6/dir_and_files/8.txt'

if (os.access(path, os.F_OK)):
    print ("This file exists")
else: 
    print("not found.")
    with open("8.txt", "x") as file:
        pass
    sleep(5)
    print ("This file exists")

sleep(5)

os.remove(path)
print ("deleted")
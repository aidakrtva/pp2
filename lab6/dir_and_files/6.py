#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import os 
path =  '/Users/aida/Documents/pp2-aida/githowto/repositories/work/lab6/dir_and_files'

os.makedirs("6files")
A = ord('A')
Z =ord('Z')
for i in range(A ,Z):
    with open(path+'/6files/' + f"{chr(i)}.txt", "w") as file:
        file.write(f"This is {chr(i)}.txt, it was created and written from 6.py")

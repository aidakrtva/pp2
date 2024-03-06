#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path
import os 
filename = "3.py"
path = os.getcwd()
#new_path = os.path.join(path, filename)
print (os.path.basename(path))
print (os.path.dirname(path))
#print (new_path)

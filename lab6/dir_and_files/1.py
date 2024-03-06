#Write a Python program to list only directories, files and all directories, files in a specified path.

import os
path = '/Users/aida/Documents/pp2-aida/githowto/repositories/work/lab6/dir_and_files'

dirs = os.listdir(path)

print(f'folders and files in path - "{path}":', dirs)
"""Write a Python program that invoke square root function after specific milliseconds.
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858
"""


import time 
from time import sleep
import math 

number = int(input())
milliseconds = int(input())

def func(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    square_root = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {square_root}")

func(number, milliseconds)
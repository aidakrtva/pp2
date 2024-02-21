#area of a parallelogram.
import math

base = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))

def area (base, height):
    res = base * height
    return res 

result  =  area(base, height)
print ("Expected Output:" , f"{result:.1f}")

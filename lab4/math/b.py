#area of trapezoid 
import math

height = int(input("Height: "))
basefirst = int(input("Base, first value: "))
basesecond = int(input("Base, second value: "))

def area(height,basefirst,basesecond):
    a = basefirst + basesecond 
    b = a / 2
    res = b * height
    return res

result = area(height,basefirst,basesecond)
print("Expected Output:", f"{result:.1f}")

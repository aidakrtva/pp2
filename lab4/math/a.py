import math

degree = float(input("Enter the degree: "))

def rad(degree):
    radian = degree * math.pi / 180
    return radian

result = rad(degree)
print("Output radian:", f"{result:.6f}")
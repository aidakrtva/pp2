#Write a Python program to calculate the area of regular polygon.
import math 

nofsides = int(input("Input number of sides: "))
lenght = int(input("Input the length of a side: "))

def apothemmmm (nofsides , lenght):
    a = 2 * math.tan(math.radians( 180 / nofsides ))
    apothem = lenght / a
    return apothem

apothem = apothemmmm(nofsides, lenght)

def area_of_poligon(nofsides , lenght , apothem):
    area = (nofsides * lenght * apothem) / 2
    return area

result = area_of_poligon(nofsides,lenght,apothem)
print("The area of the polygon is:", int(result))

"""
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
"""
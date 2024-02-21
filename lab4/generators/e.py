#Implement a generator that returns all numbers from (n) down to 0.

n = int(input(("enter the number:")))

def allnums (start, n):
    while start <= n:
        yield start
        start += 1

numbers = list (allnums(0,n))
numbers.reverse()
"""to print without commas
print (*numbers)
""" 
#and to print prettier:
print (', '.join(map(str, numbers)))

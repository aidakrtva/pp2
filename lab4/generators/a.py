#Create a generator that generates the squares of numbers up to some number N

"""
one of the solutions
nums = range (1,20)

for num in nums:
    print(num**2)
"""

def square_gen(start, stop):
    while start < stop:
        yield start ** 2 
        start += 1

square_nums = list(square_gen(1, 21))

print(square_nums)
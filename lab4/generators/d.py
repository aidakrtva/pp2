#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

start = 0 
stop = 21

def squares (start, stop):
    while start < stop:
        yield start ** 2 
        start += 1

for num in range(start, stop+1):
    for square in squares(start, stop):
        if square == num**2:
            print(f" {square}")
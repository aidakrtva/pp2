def solve(numheads, numlegs):
    c = -(numlegs-4*numheads)/2
    r = numheads-c
    return r, c

numheads = int (input())
numlegs =  int (input())
print(solve(numheads, numlegs))
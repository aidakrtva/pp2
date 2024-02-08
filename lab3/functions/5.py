from itertools import permutations

"""
def permutat(s):
    return list(permutations(s))

s = permutat(str(input()))
for i in s:
    print(i)

"""


from itertools import permutations

def permutat(s):
    return list(permutations(s))

s = "abc"
permut = permutat(s)
for i in permut:
    print(i)
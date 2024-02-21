#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def threennums(num):
    if ( num % 3 == 0):
        return num

def threegen (start,stop):
    while start <= stop:
        if threennums(start):
            yield start
        start += 1


urnum = int(input(("enter the number:")))

divbythree  = list(threegen(0, urnum))

print("numbers divisible by three are:" ,  ', '.join(map(str, divbythree)))


def fournums(num):
    if ( num % 4 == 0):
        return num

def fourgen (start,stop):
    while start <= stop:
        if fournums(start):
            yield start
        start += 1

divbyfour  = list(fourgen(0, urnum))

print("numbers divisible by four are:" ,  ', '.join(map(str, divbyfour)))



def bothnums(num):
    if ( num % 12 == 0):
        return num

def bothgen (start,stop):
    while start <= stop:
        if bothnums(start):
            yield start
        start += 1

divbyboth  = list(bothgen(0, urnum))

print("numbers divisible by 3 and 4 are:" ,  ', '.join(map(str, divbyboth)))
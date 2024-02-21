#CWrite a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def evennums(num):
    if ( num % 2 == 0):
        return num

def evengen (start,stop):
    while start <= stop:
        if evennums(start):
            yield start
        start += 1


urnum = int(input(("enter the number:")))

evennumss  = list(evengen(0, urnum))

print(', '.join(map(str, evennumss)))




a = 33
b = 200
if b > a:
  print("b is greater than a")

print ("......................")

#elif 
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
print ("......................")

#else 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#You can also have an else without the elif
print ("......................")

#Short Hand If ... Else
if a > b: print("a is greater than b")
print ("......................")

a = 2
b = 330
print("A") if a > b else print("B")
print ("......................")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
print ("......................")


#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
print ("......................")

#or 
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
print ("......................")

#not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
print ("......................")

#nested if 
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
print ("......................")

#pass statement: if u dont have anything in if statement
a = 33
b = 200

if b > a:
  pass
print (".........passused...........")

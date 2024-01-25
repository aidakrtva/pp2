fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print ("............................")

#for loop for string
for x in "banana":
  print(x)
print ("............................")

#break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
print ("............................")

#Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
print ("............................")

#continue statement. Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
print ("............................")


#range function 
for x in range(6):
  print(x)
print ("............................")

for x in range(2, 6):
  print(x)
print ("............................")
#third parametre is the step.
for x in range(2, 30, 3):
  print(x)
print ("............................")

#else in for loop 
for x in range(6):
  print(x)
else:
  print("Finally finished!")
print ("............................")
#else and break
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
print ("............................")

#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
print ("............................")


#pass statement 
for x in [0, 1, 2]:
  pass
print (".............passused...............")
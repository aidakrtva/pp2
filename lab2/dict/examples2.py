thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#all key names one by one
for x in thisdict:
  print(x)
print (".................")

#all values one by one 
for x in thisdict:
  print(thisdict[x])
print (".................")

#all values one by one 
for x in thisdict.values():
  print(x)
print (".................")

#all keys one by one 
for x in thisdict.keys():
  print(x)
print (".................")

#all keys and values one by one 
for x, y in thisdict.items():
  print(x, y)
print (".................")

#copy dicts
mydict = thisdict.copy()
print(mydict)
#and another way to do it, using fucntion dict
mydict2 = dict(thisdict)
print(mydict2)
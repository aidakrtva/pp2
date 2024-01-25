thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"]) 
print(len(thisdict))

print ("..................")

#Dictionaries cannot have two items with the same key:
blabla = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(blabla)
print ("..................")


#data types:
anotherdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(anotherdict))
print ("..................")


#another way to mace dictionary:
newdict = dict(name = "John", age = 36, country = "Norway")
print(newdict)
print ("..................")


anootherdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = anootherdict["model"]
y = anootherdict.get("model")
z = anootherdict.keys()
print (x, y, z)
print ("..................")


diict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#changing the year
diict["year"] = 2018
print (diict)
diict.update({"year": 2020})
print (diict)
print ("..................")


#adding elements
dicttt = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dicttt["color"] = "red"
print(dicttt)
dicttt.update({"secondcolor": "blue"})
print(dicttt)
print ("..................")


#remove elements
idk = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964 , 
  "color" : "yellow"
}
idk.pop("model")
print(idk)
idk.popitem() #deletes the last element from dict
print(idk)
del idk ["brand"] #deletes the specified element
print(idk)
idk.clear() #clears all dict
print (idk)
print ("..................")







thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print ("......................")


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
print ("......................")


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
print ("......................")


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
print ("......................")


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
print ("......................")


thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist) this will cause an error because you have succsesfully deleted "thislist"
print ("......................")


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print ("......................")

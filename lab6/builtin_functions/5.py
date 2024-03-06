#Write a Python program with builtin function that returns True if all elements of the tuple are true.

tuple1 = (1, True, 'hi', 3.14)
tuple2 = (0, False, '', 3.14)

print("list1, all, any:", all(tuple1))
print("list2, all, any:", all(tuple2))
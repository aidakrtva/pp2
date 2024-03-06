#Write a Python program with builtin function to multiply all the numbers in a list
nums = [1, 2, 3, 4, 5]

i= int(input("Enter the number to multiply it to the numbers in list:"))
nums_multi = list(map(lambda x : x * i , nums))


#print(*nums_multi)
print(", ".join(map(str, nums_multi)))
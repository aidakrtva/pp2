#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
#text = """aboba"""
text = str(input("Enter the text: "))
txet = reversed(text)

res = "".join(map(str,txet))

if res == text:
    print ("IT IS PALINDROME")
else : print ("it is not.")
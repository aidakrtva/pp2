from ex9 import vol
from ex10 import unique
from ex11 import palindrome
from ex13 import guess

# Volume
r = int(input())
print(vol(r))

# Uniques
l = list(map(int, input().split()))
new = unique(l)
print(new)

# Palindrome
s = input("Write a sentence to check palindrome - ")
if palindrome(s):
    print("It's a palindrome")
else:
    print("Nope, it isn't palindrome")

# Play a game
num = random.randint(1, 20)
name = input('Hello! What is your name?\n')
print(f'\nWell, {name}, I am thinking of a number between 1 and 20.')
attempts = guess(num)
print(f'\nGood job, {name}! You guessed my number in {attempts} guesses!')

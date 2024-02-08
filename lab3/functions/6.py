def rev (s):
    s.reverse()
    return s

s = input().split()

print(*(rev(s)))
# or print(" ".join(rev(s)))
import math
def vol(r):
    return (4/3) * math.pi * r**3

if __name__ == "__main__":
    r = int(input())
    print(vol(r))
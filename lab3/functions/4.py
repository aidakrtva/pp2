def pr(n):
    if n < 2 : 
        return False
    for i in range(2,  int(n**(1/2))+1):
        if n % i == 0:
           return False
    return True

def filter_prime(l):
    return [i for i in l if pr(i)]

nums = [10 , 11 , 12, 13, 14, 15,16]
primes = filter_prime(nums)

print (primes)

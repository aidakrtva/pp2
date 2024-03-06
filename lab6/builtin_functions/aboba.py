
nums = """HI Help me To Count"""

def is_capital(x):
    if(x >= 'A' and x <='Z'):
        return True
    else :
        return False

nums_iscapital = list(map( str.isupper, nums))
nums_islower= list(map( str.islower, nums))

amount_of_capitals = sum(nums_iscapital)
amount_of_lower = sum(nums_islower)

print(amount_of_capitals)
print(amount_of_lower)



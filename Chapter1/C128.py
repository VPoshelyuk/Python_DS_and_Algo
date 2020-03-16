import math

def p_norm(v, p=2):
    if p == 0: return "p can't be 0"
    sum = 0
    for num in v:
        sum += num**p
    return sum**(1/p)


print(p_norm(5, 0))
print(p_norm((5,1,3), 2))
print(p_norm([5,1], 3))
print(p_norm([3], 3))
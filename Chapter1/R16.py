def func(n):
    sum = 0
    if n <= 0: return "Wrong input!"
    for i in range(1, n):
        if i%2 == 1: sum += pow(i, 2)
    return sum 


print(func(-2))
print(func(3))
print(func(13))
print(func(20))
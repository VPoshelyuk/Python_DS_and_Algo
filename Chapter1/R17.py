def func(n):
    return sum(pow(x,2) for x in range(1, n) if x%2 == 1)


print(func(-2))
print(func(3))
print(func(13))
print(func(20))
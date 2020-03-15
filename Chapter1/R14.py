def sq(n):
    sum = 0
    if n <= 0:
        return "Wrong input!"
    for i in range(1, n):
        sum += pow(i, 2)
    return sum 

print(sq(-2))
print(sq(3))
print(sq(13))
print(sq(20))
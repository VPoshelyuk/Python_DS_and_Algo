def sq(n):
    return sum(pow(x,2) for x in range(1, n))

print(sq(-2))
print(sq(3))
print(sq(13))
print(sq(20))
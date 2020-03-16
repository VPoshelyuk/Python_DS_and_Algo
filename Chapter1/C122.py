import random

def dotProduct(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return c

print(dotProduct([12,4,54,-3],[14,12,76,22]))
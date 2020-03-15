def minmax(data):
    min = float('inf')
    max = float('-inf')
    for element in data:
        if element < min:
            min = element
        if element > max:
            max = element 
    return min, max 

print(minmax((13,21,3,31)))
print(minmax((20,5,4,-2,7)))
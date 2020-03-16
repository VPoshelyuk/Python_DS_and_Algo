def arrayIndex(array, index, value = 100):
    try:
        array[index] = value
    except IndexError:
        print ("Don't try buffer overflow attacks in Python!")

array = [12,4,54,-3]
arrayIndex(array, 3)
arrayIndex(array, 30, 9)
arrayIndex(array, 0, 9)
print(array)
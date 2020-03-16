from timeit import Timer

def reverseList(data):
    i = 0
    while i < len(data)/2:
        data[i], data[len(data) - 1 - i] = data[len(data) - 1 - i], data[i]
        i+=1
    return data

data = [12,4,54,-3,14,12,76,22]
print(Timer(lambda: reverseList(data)).timeit()) #1.88612833
print(Timer(lambda: list(reversed(data))).timeit()) #0.4288700219999999
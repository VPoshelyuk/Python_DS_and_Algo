import random

def shuffle(data):
    for i in range(len(data)):
        choice = random.randint(0, len(data)-1-i)
        data[i], data[len(data)-1-choice] = data[len(data)-1-choice], data[i]
    return data

print(shuffle([12,4,54,-3,14,12,76,22]))
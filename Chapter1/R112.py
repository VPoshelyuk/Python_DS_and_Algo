import random

def randchoice(data):
    return data[random.randrange(0, len(data))]

print(randchoice([12,4,54,-3,14,12,76,22]))
def pairs(data):
    curr_odd = None
    for number in data:
        if number % 2 == 1:
            if number != curr_odd and not curr_odd is None: return curr_odd, number
            else: curr_odd = number
    return 'Not found'


data = [1,2,3,4,5,6,7]
print(pairs(data))
def distinct(data):
    data_set = set(data)
    if len(data) == len(data_set): return True
    return False


data = [1,2,3,6,7]
f_data = [1,2,3,1,6,7]
print(distinct(data))
print(distinct(f_data))
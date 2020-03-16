def scale(data, factor):
    for val in data:
        val *= factor
    return data

def rscale(data, factor):
    for el in range(len(data)):
        data[el] *= factor
    return data


data = [1,2,3,6,7]
print(scale(data, 5))
print(rscale(data, 5))
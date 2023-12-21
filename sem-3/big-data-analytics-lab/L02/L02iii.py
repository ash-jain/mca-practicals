def map(data):
    res = []

    for key, value in data:
        res.append({value: 1})

    return res


def reduce(data):
    res = {}

    for pair in data:
        a, b = list(pair.items())[0]
        if a not in res:
            res[a] = 0
        res[a] += b

    return res


filename = 'document.txt'

data = []

with open(filename, 'r') as file:
    data.extend([(filename[0].upper(), word.lower()) for word in file.read().strip().split(' ')])

print(f"Map input: {data}\n")
mapOutput = map(data)
print(f"Map output/Reduce input: {mapOutput}\n")
reduceOutput = reduce(mapOutput)
print(f"Final output: {reduceOutput}")

def map(data):
    res = []

    for key, value in data:
        res.append({key: int(value[2])})

    return res


def shuffle_and_sort(data):
    res = {}

    for pair in data:
        a, b = list(pair.items())[0]
        if a not in res:
            res[a] = []
        res[a].append(b)

    return res


def reduce(data):
    res = {}

    for key, value in data.items():
        res[key] = sum(value)

    return res


raw_data = """Pratap Fan 1500
Sangram Fridge 20000
Rahul Mobile 15000
Kishor Furniture 55000
Sangram Oven 7000
Rahul Tablet 25000
Pratap Camera 12000
Sangram Laptop 67000
Kishor AirConditioner 34000
Pratap Printer 8000
Sangram DinningTable 29000
Rahul HomeTheater 18000
Sangram DVDPlayer 3000"""

data = [(item.split(' ')[0], item.split(' ')) for item in raw_data.split('\n')]

print(f"Map input: {data}\n")

mapOutput = map(data)
print(f"Map output:{mapOutput}\n")

reduceInput = shuffle_and_sort(mapOutput)
print(f"Reduce input: {reduceInput}\n")

finalOutput = reduce(reduceInput)
print(f"Reduce output: {finalOutput}")

def map(data, friends):
    res = []

    for key, connections in data.items():
        if key not in friends:
            continue
        for connection in connections:
            res.append({connection: key})

    return res


def reduce(data):
    res = {}

    for item in data:
        for key, value in item.items():
            if key not in res:
                res[key] = []
            res[key].append(value)

    return {key: key for key, value in res.items() if len(value) == 2}


dictionary = {
    "A": ["B", "C", "D"],
    "B": ["A", "C", "D", "E"],
    "C": ["A", "B", "D", "E"],
    "D": ["A", "B", "C", "E"],
    "E": ["B", "C", "D"],
}

friends = {"A", "B"}

mapOutput = map(dictionary, friends)
print(f"Map Output: {mapOutput}")
print(f"Reduce Output: {reduce(mapOutput)}")

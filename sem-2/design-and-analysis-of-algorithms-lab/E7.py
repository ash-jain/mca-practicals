"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Design and Analysis of Algorithms Lab.
* Lab Experiment No. 7 - Finding the shortest path in a graph using Dijkstra's algorithm. Take inputs from user.
"""

import heapq


def dijkstras_algorithm(adjMatrix, root, target):
    distances = dict(
        (i, float("inf")) if i != root else (root, 0) for i in range(len(adjMatrix))
    )
    queue = [tup[::-1] for tup in distances.items()]

    while queue:
        heapq.heapify(queue)
        dist, curr = heapq.heappop(queue)

        for node, weight in enumerate(adjMatrix[curr]):
            if weight > 0 and distances[node] > dist + weight:
                queue[queue.index((distances[node], node))] = (dist + weight, node)
                distances[node] = dist + weight

    return distances[target]


if __name__ == "__main__":
    nodes = int(input("Input the number of nodes: "))
    number_of_edges = int(input("Input the number of edges: "))

    matrix = [[0 for i in range(nodes)] for j in range(nodes)]

    print('Enter the edges in the format "node1 node2 weight":')
    for _ in range(number_of_edges):
        a, b, w = list(map(int, input().split(" ")))
        matrix[a][b] = w
        matrix[b][a] = w

    node, target = list(map(int, input("Enter the root and target node: ").split(" ")))

    print(
        f"Distance between {node} and {target} is: {dijkstras_algorithm(matrix, node, target)}"
    )


# dijkstras_algorithm([
#     [0, 4, 0, 0, 0, 0, 0, 8, 0],
#     [4, 0, 8, 0, 0, 0, 0, 11, 0],
#     [0, 8, 0, 7, 0, 4, 0, 0, 2],
#     [0, 0, 7, 0, 9, 14, 0, 0, 0],
#     [0, 0, 0, 9, 0, 10, 0, 0, 0],
#     [0, 0, 4, 14, 10, 0, 2, 0, 0],
#     [0, 0, 0, 0, 0, 2, 0, 1, 6],
#     [8, 11, 0, 0, 0, 0, 1, 0, 7],
#     [0, 0, 2, 0, 0, 0, 6, 7, 0]
# ], 0, 1)

"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Design and Analysis of Algorithms Lab.
* Lab Experiment No. 8. - Find all pair shortest path using Floyd Warshall algorithm.
"""


def floydWarshall(adjMatrix):

    for k in range(len(adjMatrix)):
        for i in range(len(adjMatrix)):
            for j in range(len(adjMatrix)):
                adjMatrix[i][j] = min(adjMatrix[i][j], adjMatrix[i][k] + adjMatrix[k][j])

    return adjMatrix


adjMatrix = [[float('inf'), 10, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 8],
[float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 2, float('inf'), float('inf')],
[float('inf'), 1, float('inf'), 1, float('inf'), float('inf'), float('inf'), float('inf')],
[float('inf'), float('inf'), float('inf'), float('inf'), 3, float('inf'), float('inf'), float('inf')],
[float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), -1, float('inf'), float('inf')],
[float('inf'), float('inf'), -2, float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
[float('inf'), -4, float('inf'), float('inf'), float('inf'), -1, float('inf'), float('inf')],
[float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 1, float('inf')]]

for i in range(len(adjMatrix)):
    adjMatrix[i][i] = 0


[print(row) for row in floydWarshall(adjMatrix)]

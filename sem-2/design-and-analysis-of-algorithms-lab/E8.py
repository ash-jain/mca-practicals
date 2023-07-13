"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Design and Analysis of Algorithms Lab.
* Lab Experiment No. 8. - Implement the solutions to the following using dynamic programming approach: Finding the shortest path in a graph with negative edge weights. (Bellman-Ford's algorithm)
"""


def bellman_ford_algorithm(nodes, adj_matrix, source, target):
    dp = [float("inf")] * (nodes - 1)
    dp[source] = 0

    for i in range(nodes - 1):
        for a in range(len(adj_matrix)):
            for b in range(len(adj_matrix[i])):
                if adj_matrix[a][b]:
                    dp[b] = min(dp[b], dp[a] + adj_matrix[a][b])

    print(dp)
    return dp[target]


nodes = 9

adj_matrix = [
    [0, 10, 0, 0, 0, 0, 0, 8],
    [0, 0, 0, 0, 0, 2, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0],
    [0, 0, -2, 0, 0, 0, 0, 0],
    [0, -4, 0, 0, 0, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
]

source, target = 0, 4

print(
    f"Distance of {target} from {source} is {bellman_ford_algorithm(nodes, adj_matrix, source, target)}"
)

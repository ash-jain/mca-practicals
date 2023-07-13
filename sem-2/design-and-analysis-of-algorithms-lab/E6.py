"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Design and Analysis of Algorithms Lab.
* Lab Experiment No. 6 - Traverse any given graph using Depth First Search (DFS).
"""

from collections import deque


def depth_first_search(adjList, startNode):
    stack = deque([startNode])
    visited = set([startNode])
    res = []

    while stack:
        node = stack.pop()
        res.append(node)

        for edge in adjList[node]:
            if edge not in visited:
                stack.append(edge)
                visited.add(edge)

    return res


if __name__ == "__main__":
    adjList = {
        1: [2, 3, 4],
        2: [1, 3],
        3: [1, 2],
        4: [1, 5, 8],
        5: [4, 6, 7],
        6: [5, 7, 8, 9],
        7: [5, 6],
        8: [4, 6, 9],
        9: [6, 8, 10],
        10: [9],
    }

    print(f"Depth first traversal of the given adjacency list: {depth_first_search(adjList, 1)}.")

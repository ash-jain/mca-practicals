"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Design and Analysis of Algorithms Lab.
* Lab Experiment No. 5 - Traverse any given graph using Breadth First Search(BFS).
"""

from collections import deque
kp

def breadth_first_search(adjList, startNode):
    q = deque([startNode])
    visited = set([startNode])
    res = []

    while q:
        node = q.popleft()
        res.append(node)

        for edge in adjList[node]:
            if edge not in visited:
                q.append(edge)
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

    print(f"Breadth first traversal of the given adjacency list: {breadth_first_search(adjList, 1)}.")

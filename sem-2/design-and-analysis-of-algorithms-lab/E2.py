"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Design and Analysis of Algorithms.
* Lab Experiment No. 2 - Implement selection sort using recursion.
Take input from User.
"""


def selection_sort(arr, r):
    if r < 1:
        return arr

    max_index = 0

    for i in range(r):
        if arr[max_index] < arr[i]:
            max_index = i

    arr[max_index], arr[r - 1] = arr[r - 1], arr[max_index]

    return selection_sort(arr, r - 1)


if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: \n").split(" ")))
    print("\nAfter sorting:")
    print(selection_sort(arr, len(arr)))
k

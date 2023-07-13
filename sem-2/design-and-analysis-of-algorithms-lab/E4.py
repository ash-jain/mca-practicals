"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Design and Analysis of Algorithms Lab.
* Lab Experiment No. 4 - Implement the solution to the following using Quicksort algorithm: 
Counting inversions to sort n numbers.
Attach the output for each of the following data.
"""

data = """1 2 3 4 5 6 7 8 9 10
10 9 8 7 6 5 4 3 2 1
6 3 8 5 1 9 4 10 7 2
9 10 3 4 5 6 7 8 1 2
2 3 4 5 6 7 8 9 10 1
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
16 1 4 2 12 9 10 3 5 24 14 20 6 23 7 25 19 18 8 22 11 17 13 15 21
24 25 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 1 2
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 1"""

def quick_sort(arr, left, right):

    if left >= right:
        return 0

    pivot = arr[left]
    arr[left], arr[right] = arr[right], arr[left]
    inversions = 1
    ptr = 0

    for i in range(right):
        if arr[i] < pivot:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
            inversions += 1

    arr[right], arr[ptr] = arr[ptr], arr[right]
    inversions += 1

    inversions += quick_sort(arr, left, ptr-1)
    inversions += quick_sort(arr, ptr+1, right)

    return inversions


if __name__ == "__main__":

    test_data = [list(map(int, arr.split(' '))) for arr in data.split('\n')]

    for arr in test_data:
        print('Unsorted data:', arr)
        n = quick_sort(arr, 0, len(arr)-1)
        print('Sorted data:', arr)
        print('Inversions:', n, '\n')

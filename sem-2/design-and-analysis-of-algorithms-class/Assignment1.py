"""Q. 1 Write the algorithm for insertion sort (L to R search) and do a dry run for sorted, and random data of size 10. Write the number of comparisons and number of moves."""

def insertion_sort(arr):

    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            j = i - 1
            value = arr[i]

            while j >= 0 and arr[j] > value:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = value

    return arr


def reverse_insertion_sort(arr):

    for i in range(len(arr)-2, -1, -1):
        if arr[i] > arr[i+1]:
            j = i + 1
            value = arr[i]

            while j < len(arr) and arr[j] < value:
                arr[j-1] = arr[j]
                j += 1

            arr[j-1] = value

    return arr


def binary_search(arr, value, left, right):
    while left < right:
        pivot = (left + right) // 2
        if arr[pivot] <= value:
            left = pivot + 1
        else:
            right = pivot
    return right


def insertion_sort_with_binary_search(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            index = binary_search(arr, arr[i], 0, i-1)
            value = arr[i]
            j = i - 1
            while j >= index:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = value
    return arr

import random

# print(insertion_sort_with_binary_search([10, 19, 23, 39, 46, 56, 65, 72, 86, 92]))

print(insertion_sort_with_binary_search([random.randrange(100) for _ in range(10)]))
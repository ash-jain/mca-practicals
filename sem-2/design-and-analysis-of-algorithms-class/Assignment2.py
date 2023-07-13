def quick_sort(arr, left = None, right = None):
    if left is None or right is None:
        left = 0
        right = len(arr)

    if left + 1 >= right:
        return None

    pivot = left

    for i in range(left+1, right):
        if arr[i] <= arr[pivot]:
            arr[i], arr[left+1] = arr[left+1], arr[i]
            left += 1

    arr[pivot], arr[left] = arr[left], arr[pivot]

    quick_sort(arr, pivot, left)
    quick_sort(arr, left+1, right)


from collections import deque

def quick_sort_iterative(arr):

    q = deque([(0, len(arr))])

    while q:
        left, right = q.popleft()

        if left + 1 >= right:
            continue

        pivot = left

        for i in range(left+1, right):
            if arr[i] <= arr[pivot]:
                arr[i], arr[left+1] = arr[left+1], arr[i]
                left += 1

        arr[pivot], arr[left] = arr[left], arr[pivot]

        q.append((pivot, left))
        q.append((left+1, right))


arr1 = [20,10,5,30,40,57, 35, 25, 18, 22, 21, 3]
arr2 = [20,10,5,30,40,57, 35, 25, 18, 22, 21, 3]
quick_sort(arr1)
quick_sort_iterative(arr2)
print(arr1 == arr2)

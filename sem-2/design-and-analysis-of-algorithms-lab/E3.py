"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Design and Analysis of Algorithms.
* Lab Experiment No. 3 - Implement the solution to the following using divide and conquer approach:
A. Sorting given data using merge sort.
"""

class MergeSort:
    def merge(self, arr1, arr2):
        arr = []
        l, r = 0, 0
        while l < len(arr1) and r < len(arr2):
            if arr1[l] < arr2[r]:
                arr.append(arr1[l])
                l += 1
            else:
                arr.append(arr2[r])
                r += 1
        arr.extend(arr1[l:])
        arr.extend(arr2[r:])
        return arr

    def merge_sort(self, arr, l=0, r=None):
        if r is None:
            r = len(arr)

        if r - l <= 1:
            return [arr[l]]

        mid = (l + r) // 2
        L = self.merge_sort(arr, l, mid)
        R = self.merge_sort(arr, mid, r)

        return self.merge(L, R)


if __name__ == "__main__":
    ms = MergeSort()
    arr = list(map(int, input('Enter numbers separated by spaces: ').split(' ')))
    print('After Sorting: ')
    print(ms.merge_sort(arr))



# def merge_sort(arr, l = 0, r = None):
#     if r is None:
#         r = len(arr)
#     if r - l <= 1:
#         return None

#     print(arr[l:r])

#     merge_sort(arr, l, (l+r) // 2)
#     merge_sort(arr, (l+r) // 2, r)

#     i, j = l, (l+r) // 2
#     k = l

#     while k < r:
#         if j == r or arr[i] <= arr[j]:
#             i += 1
#         elif i == (l+r) // 2 or arr[j] < arr[i]:
#             arr.insert(k, arr.pop(j))
#             i += 1
#             k += 1

#     print(arr[l:r])
# helper function
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range(0, elements):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


arrA = [1, 5, 6, 9, 1, 2]
arrB = [10, 51, 16, 9, 1, 12]

# recursive sorting function


def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) / 2])
        right = merge_sort(arr[0:len(arr) / 2:])
        arr = merge(left, right)   # merge() defined later
    return arr


arr = [1, 5, 6, 9, 1, 2]
merge_sort(arr)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below
def split(arr, low, high):
    i = low(low-i)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[high], arr[i+1]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quick_sort(arr, low, high):
    if low < high:
        si = split(arr, low, high)

        quick_sort(arr, low, si-1)
        quick_sort(arr, si+1, high)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

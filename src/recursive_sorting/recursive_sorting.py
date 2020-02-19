# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []# TO-DO
    i, j, counter = 0
    arr_a_complete = False
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[counter] = arrA[i]
            i += 1
            counter += 1
            arr_a_complete = True
        else:
            merged_arr[counter] = arrB[j]
            j += 1
            counter += 1
            arr_a_complete = False

    if arr_a_complete:
        merged_arr += arrB[j:]
    else:
        merged_arr += arrA[i:]
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr

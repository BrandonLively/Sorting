# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements

    for i in range(0, len(arr)):
        small_index = i
        curr_num = arr[i]
        for j in range(i, len(arr)):
            small_index
            if arr[j] < arr[small_index]:
                small_index = j
        small_num = arr[small_index]
        arr[i] = small_num
        arr[small_index] = curr_num
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    counter = 0
    for i in range(1, len(arr)):
        for j in range(1, len(arr) - counter):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr

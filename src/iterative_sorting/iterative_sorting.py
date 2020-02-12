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
    for i in range(1, len(arr) - counter):
        if arr[i] < arr[i - 1]:
            pos1 = arr[i - 1]
            pos2 = arr[i]
            arr[i - 1] = pos2
            arr[i] = pos1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr


test_arr = [7, 6, 56, 3, 21, 2, 45, 23, 34, 6, 86, 62134, 3, 35, 24, 5, 2, 42, 6, 23, 4, 6, 2345, 23, 6523, 42, 23523,
            457, 54, 325, 23, 523, 5]

print(selection_sort(test_arr))

print(bubble_sort(test_arr))

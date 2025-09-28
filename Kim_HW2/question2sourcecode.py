import time

from datetime import datetime

# global variable to track comparisons
comparisons = 0

# resets global variable function


def reset_comparisons():
    global comparisons
    comparisons = 0

# get global variable (comparisons) function


def get_comparisons():
    global comparisons
    return comparisons

# insertion sort function


def insertionSort(arr):
    global comparisons

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # move elements of arr[0..i-1], that are greater than key, to one position ahead
        # of their current position
        while j >= 0:
            comparisons += 1
            if key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break

        arr[j + 1] = key

# merge function


def merge(arr, left, mid, right):
    global comparisons

    n1 = mid - left + 1
    n2 = right - mid

    # create temp arrays
    L = [0] * n1
    R = [0] * n2

    # copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    # merge the temp arrays back into arr[left..right]
    while i < n1 and j < n2:
        comparisons += 1

        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

        k += 1

    # copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# mergeSort function


def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)


# function to read file and return values as a list
def read_file(filename):
    # open the file
    with open(filename, "r") as file:
        content = file.read()
        string_nums = content.split()
        return list(map(int, string_nums))

# time efficiency function, returns time it takes for function to complete


def timeEfficiency(funcName, *args, **kwargs):
    start_time = time.perf_counter()

    result = funcName(*args, **kwargs)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    return elapsed_time

# testing the insertion sort in this function


def test_insertion(filename):
    # read the data
    data = read_file(filename)

    # make a copy array since sorting modifies the array
    data_copy_array = data.copy()

    # reset number of comparisons before starting
    reset_comparisons()

    execution_time = timeEfficiency(insertionSort, data_copy_array)

    comparison_count = get_comparisons()

    return execution_time, comparison_count

# testing the merge sort in this function


def test_merge(filename):
    # read the data
    data = read_file(filename)

    # make a copy array since sorting modifies array
    data_copy_array = data.copy()

    # reset number of comparisons before starting
    reset_comparisons()

    execution_time = timeEfficiency(
        mergeSort, data_copy_array, 0, len(data_copy_array) - 1)

    comparison_count = get_comparisons()

    return execution_time, comparison_count


if __name__ == "__main__":

    # note: i commented file_names out so it wouldn't run for 8 hours 😭
    # file_names = ["rand1000.txt", "rand10000.txt", "rand100000.txt", "rand250000.txt", "rand500000.txt", "rand1000000.txt"]

    # using data that won't take a while to run
    file_names = ["rand1000.txt", "rand10000.txt"]

    insertion_results = []
    merge_results = []

    for file_name in file_names:
        print(f"Testing {file_name}")

        # append result data from insertion sort as a tuple
        insertion_time, insertion_comparison = test_insertion(file_name)
        insertion_results.append((insertion_time, insertion_comparison))

        # append result data from merge sort as a tuple
        merge_time, merge_comparison = test_merge(file_name)
        merge_results.append((merge_time, merge_comparison))

    print("\nInsertion Results:")
    print(insertion_results)
    print("\nMerge Results:")
    print(merge_results)

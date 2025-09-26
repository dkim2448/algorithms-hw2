# Global variable to track comparisons
comparisons = 0

# Insertion sort function


def insertionSort(arr):
    global comparisons

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0:
            comparisons += 1
            if key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break

        arr[j + 1] = key

# A utility function to print array of size n


def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

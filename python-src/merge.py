def mergeSort(A):
    if(len(A)<=1):
        return A
    half_i = round(len(A)/2)
    left = list(A[:half_i])
    right = list(A[half_i:])
    left_sorted = mergeSort(left)
    right_sorted = mergeSort(right)
    newArr = []
    while len(left_sorted)>0 and len(right_sorted)>0:
        if(left_sorted[0]<right_sorted[0]):
            newArr.append(left_sorted.pop(0))
        else:
            newArr.append(right_sorted.pop(0))
    if len(left_sorted)==0:
        newArr.extend(right_sorted)
    else:
        newArr.extend(left_sorted)
    return newArr

def sort(A):
    test = mergeSort(A)
    # print(A.compares)
    # print(test)

    # Do quicksort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.

    return A

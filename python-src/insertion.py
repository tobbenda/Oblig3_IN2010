# Velg elem = index 1
# while elem > elem-1
# swap elem og elem-1
# indexen til elem er indexen til elem -1


def insertionSort(A):
    for i in range(0, len(A)):
        index=i
        while A[index] <= A[index-1] and index >0:
            A.swap(index, index-1)
            index = index-1
    return A
    

def sort(A):
    test = insertionSort(A)

    # Do insertion sort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.

    return A

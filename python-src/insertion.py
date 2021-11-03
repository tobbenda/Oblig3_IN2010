def insertionSort(A):
    for i in range(0, len(A)):
        index=i
        while A[index] <= A[index-1] and index >0:
            A.swap(index, index-1)
            index = index-1
    return A
    

def sort(A):
    insertionSort(A)
    return A

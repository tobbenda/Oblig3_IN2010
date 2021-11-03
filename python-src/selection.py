def selectionSort(A):
    min_i = 0
    while min_i < len(A)-1:
        currVal = A[min_i]
        currInd = min_i+1
        for j in range(min_i, len(A)):
            if A[j]<currVal:
                currVal = A[j]
                currInd = j
        if(A[min_i]>A[currInd]):
            A.swap(min_i, currInd)
        min_i +=1
    return A


def sort(A):
    selectionSort(A)
    return A




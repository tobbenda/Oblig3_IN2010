def quickSort(A):
    if(len(A)<=1):
        return A
    pivot = A[round(len(A)/2)]
    A.remove(pivot)
    lesserList = []
    greaterList = []
    for num in A:
        if num<pivot:
            lesserList.append(num)
        else:
            greaterList.append(num)
    return (quickSort(lesserList)+ [pivot] + quickSort(greaterList))

def partition(A, low, high):
    index = low-1
    pivot = A[high]
    for x in range(low, high):
        if A[x]<pivot:
            index += 1
            A.swap(x, index)
    A.swap(index+1, high)
    return index+1

def quickSortInPlace(A, low=0, high = None):
    if high == None:
        high = len(A)-1
    if low < high:
        p_index = partition(A, low, high)
        quickSortInPlace(A, low, p_index-1)
        quickSortInPlace(A, p_index+1, high)
    return A

def sort(A):
    quickSortInPlace(A)

    return A

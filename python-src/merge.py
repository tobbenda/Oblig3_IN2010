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
    result=mergeSort(A)
    return result


def __merge(arr, l, mid, r):

    aux = arr[l:r + 1]
    i = l
    j = mid + 1

    for k in range(l, r + 1):
        if i > mid:
            arr[k] = aux[j - l]
            j += 1
        elif j > r:
            arr[k] = aux[i - l]
            i += 1
        
        elif aux[i - l] < aux[j - l]:
            arr[k] = aux[i - l]
            i += 1
        else:
            arr[k] = aux[j - l]
            j += 1


def __mergeSort(arr, l, r):

    if l >= r:
        return
    
    mid = (l + r) // 2
    __mergeSort(arr, l, mid)
    __mergeSort(arr, mid + 1, r)
    __merge(arr, l, mid, r)


def mergeSort(arr):
    
    __mergeSort(arr, 0, len(arr) - 1)


arr = [8, 7, 6, 5, 4, 3, 2, 1, 100, 200, 500, 1, 203021, 2034]
print("Before: ", arr)
mergeSort(arr)
print("After using mergeSort: ", arr)



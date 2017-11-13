def __partition(arr, l, r):

    v = arr[l]

    j = l
    for i in range(l + 1, r + 1):
        if arr[i] < v:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[l], arr[j] = arr[j], arr[l]

    return j


def __quickSort(arr, l, r):

    if l >= r:
        return
    
    pos = __partition(arr, l, r)
    __quickSort(arr, l, pos - 1)
    __quickSort(arr, pos + 1, r)


def quickSort(arr):

    return __quickSort(arr, 0, len(arr) - 1)


a = [8, 7, 6, 5, 4, 3, 2, 1]
print("Before: ", a)
quickSort(a)
print("After using quickSort", a)




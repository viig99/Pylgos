def mergesort(arr):
    """ perform mergesort on a list of numbers 

    >>> mergesort([5, 4, 1, 6, 2, 3, 9, 7])
    [1, 2, 3, 4, 5, 6, 7, 9]

    >>> mergesort([3, 2, 4, 2, 1])
    [1, 2, 2, 3, 4]
    """
    n = len(arr)
    if n <= 1: return arr
    a1 = arr[:n/2]
    a2 = arr[n/2:]
    a1 = mergesort(a1)
    a2 = mergesort(a2)
    return merge(a1, a2)

def merge(arr_a, arr_b):
    arr_c = []
    i, j = (0, 0)
    while i < len(arr_a) and j < len(arr_b):
        if arr_a[i] <= arr_b[j]:
            arr_c.append(arr_a[i])
            i += 1
        else:
            arr_c.append(arr_b[j])
            j += 1
    if arr_a[i:]: arr_c += arr_a[i:]
    if arr_b[j:]: arr_c += arr_b[j:]
    return arr_c

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

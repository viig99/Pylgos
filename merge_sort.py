
def mergeSort(a):
	if len(a) <= 1:
		return a
	a1 = a[:len(a)/2]
	a2 = a[len(a)/2:]
	a1 = mergeSort(a1)
	a2 = mergeSort(a2)
	return merge(a1,a2)
	
def merge(a, b):
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if a:
        c.extend(a[i:])
    if b:
        c.extend(b[j:])
    return c

if __name__ == "__main__":
	y = mergeSort([1,3,4,5,6,7,2])
	print(y)
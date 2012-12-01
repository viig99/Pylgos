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

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1 
        key = l[i]
        while l[j] > key and j >= 0:
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
	return l
	
def selection_sort(l):
	for i in range(0,len(l)-1):
		mn = min(range(i,len(l)), key=l.__getitem__)
		l[i],l[mn] = l[mn],l[i]
	return l
	
def quicksort(l):
	if len(l) <= 1:
		return l
	else:
		from random import randrange
		pivot = l.pop(randrange(len(l)))
		lower = quicksort([x for x in l if x < pivot])
		greater = quicksort([x for x in l if x >= pivot])
		return lower + [pivot] + greater
		
def quicksort_part(A,s,e):
	if e-s > 1:
		from random import randint
		p = A[randint(s+1,e)]
		A[p], A[s] = A[s], A[p]
		pp = part_quick(A,s,e)
		quicksort_part(A,s,pp-1)
		quicksort_part(A,pp,e)

def part_quick(A,l,r):
	p, i = A[l], l+1
	for j in range(i,r+1):
		if A[j] < p:
			A[j] , A[i] = A[i], A[j]
			i += 1
	A[l], A[i-1] = A[i-1], A[l]
	return i-1
		
if __name__ == "__main__":
	A = [1,3,4,5,6,7,2,1,5]
	y = quicksort_part(A,0,8)
	print(A)
def quicksort(A):
    actual_quicksort(A, 0, len(A))

def actual_quicksort(A, begin, end):
    if end - begin > 1:
        edge = hoare_half_partition(A, begin, end)
        actual_quicksort(A, begin, edge)
        actual_quicksort(A, edge + 1, end)

def partition(A, begin, end):
    pivot = A[end - 1]
    i = begin
    for j in range(begin, end - 1):
        if A[j] <= pivot:
            A[j], A[i] = A[i], A[j]
            i = i + 1
    A[i], A[end - 1] = A[end - 1], A[i]
    return i

def hoare_half_partition(A, begin, end):
    pivot = A[(begin + end) // 2]
    i = begin
    j = end - 1
    while True:
        while A[i] < pivot:
            i = i + 1
        while pivot < A[j]:
            j = j - 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j

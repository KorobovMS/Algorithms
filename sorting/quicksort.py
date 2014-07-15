def quicksort(A):
    actual_quicksort(A, 0, len(A))

def actual_quicksort(A, begin, end):
    if end - begin > 1:
        edge = partition(A, begin, end)
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

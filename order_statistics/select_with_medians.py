def select_with_medians(A, k):
    return actual_select(A, 0, len(A), k)

def actual_select(A, begin, end, k):
    if end - begin == 1:
        return A[begin]

    medians = []
    i = 0
    elem_grp = 5
    while i < (end - begin) // elem_grp:
        insertion_sort(A, begin + i*elem_grp, begin + (i + 1)*elem_grp)
        medians.append(A[begin + i*elem_grp + (elem_grp - 1) // 2])
        i = i + 1
    rest = end - (begin + i*elem_grp)
    if rest != 0:
        insertion_sort(A, begin + i*elem_grp, end)
        medians.append(A[begin + i*elem_grp + (rest - 1) // 2])
    median = actual_select(medians, 0, len(medians), (len(medians) - 1) // 2)
    edge = partition(A, begin, end, median) + 1
    if k == edge - begin:
        return median
    elif k < edge - begin:
        return actual_select(A, begin, edge, k)
    else:
        return actual_select(A, edge, end, k - edge + begin)


def insertion_sort(A, begin, end):
    for i in range(begin + 1, end):
        key = A[i]
        j = i - 1
        while j >= begin and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key

def partition(A, begin, end, pivot):
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


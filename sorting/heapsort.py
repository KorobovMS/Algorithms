def heapsort(A):
    heapify(A)
    end = len(A) - 1
    while end > 0:
        A[0], A[end] = A[end], A[0]
        end = end - 1
        siftDown(A, 0, end)

def heapify(A):
    start = int((len(A) - 2)/2)
    while start >= 0:
        siftDown(A, start, len(A) - 1)
        start = start - 1

def siftDown(A, start, end):
    root = start
    while 2*root + 1 <= end:
        child = 2*root + 1
        swap = root
        if A[swap] < A[child]:
            swap = child
        if child + 1 <= end and A[swap] < A[child + 1]:
            swap = child + 1
        if swap != root:
            A[root], A[swap] = A[swap], A[root]
            root = swap
        else:
            return

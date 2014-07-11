def mergesort(A):
    actual_mergesort(A, 0, len(A))

# sort subarray of A with indices [begin, end)
def actual_mergesort(A, begin, end):
    if (end - begin > 1):
        mid = (begin + end) // 2
        actual_mergesort(A, begin, mid)
        actual_mergesort(A, mid, end)
        merge(A, begin, mid, end)

# merge subarrays A[begin, mid), A[mid, end)
def merge(A, begin, mid, end):
    left = [Element(A[idx]) for idx in range(begin, mid)] + [Element()]
    right = [Element(A[idx]) for idx in range(mid, end)] + [Element()]

    left_idx = 0
    right_idx = 0
    for idx in range(begin, end):
        if left[left_idx] < right[right_idx]:
            A[idx] = left[left_idx].element
            left_idx = left_idx + 1
        else:
            A[idx] = right[right_idx].element
            right_idx = right_idx + 1

class Element:
    def __init__(self, element=None):
        self.is_sentinel = element is None
        self.element = element

    def __lt__(self, other):
        if self.is_sentinel:
            return False
        if other.is_sentinel:
            return True
        return self.element < other.element

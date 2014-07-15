def maximum_subarray(A):
    return find_maximum_subarray(A, 0, len(A))

def find_maximum_subarray(A, begin, end):
    if end - begin == 1:
        return (begin, end, A[begin])
    else:
        mid = (begin + end) // 2
        left_begin, left_end, left_sum = \
            find_maximum_subarray(A, begin, mid)
        right_begin, right_end, right_sum = \
            find_maximum_subarray(A, mid, end)
        cross_begin, cross_end, cross_sum = \
            find_maximum_crossing_subarray(A, begin, mid, end)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_begin, left_end, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_begin, right_end, right_sum)
        else:
            return (cross_begin, cross_end, cross_sum)

def find_maximum_crossing_subarray(A, begin, mid, end):
    left_sum = A[mid - 1]
    max_left = mid - 1
    summ = A[mid - 1]
    for i in range(mid - 2, begin - 1, -1):
        summ = summ + A[i]
        if summ > left_sum:
            left_sum = summ
            max_left = i

    right_sum = A[mid]
    max_right = mid
    summ = A[mid]
    for i in range(mid + 1, end):
        summ = summ + A[i]
        if summ > right_sum:
            right_sum = summ
            max_right = i

    return (max_left, max_right + 1, left_sum + right_sum)

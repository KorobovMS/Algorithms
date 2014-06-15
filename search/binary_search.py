def binary_search(seq, elem):
    left = 0
    right = len(seq) - 1
    ex = ValueError('{} not found'.format(elem))
    if len(seq) == 0:
        raise ex
    while left <= right:
        mid = (left + right) // 2
        if seq[mid] == elem:
            return mid
        if seq[mid] < elem:
            left = mid + 1
        else:
            right = mid - 1
    raise ex

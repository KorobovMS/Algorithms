def select_by_sorting(seq, k):
    sorted_seq = sorted(seq)
    order = 1
    idx = 0
    if len(sorted_seq) == 0:
        raise ValueError('Empty list has no order statistics')
    while idx + 1 < len(sorted_seq) and order < k:
        if sorted_seq[idx] != sorted_seq[idx + 1]:
            order = order + 1
        idx = idx + 1
    if order == k:
        return sorted_seq[idx]
    else:
        raise ValueError('{}-order statistic does not exist'.format(k))

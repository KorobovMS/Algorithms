from random import randrange

def randomized_select(seq, k):
    return actual_randomized_select(seq, 0, len(seq), k)

def actual_randomized_select(seq, begin, end, k):
    if end - begin == 1:
        return seq[begin]
    edge = randomized_partition(seq, begin, end)
    length = edge - begin + 1
    if k == length:
        return seq[edge]
    elif k < length:
        return actual_randomized_select(seq, begin, edge, k)
    else:
        return actual_randomized_select(seq, edge + 1, end, k - length)

def randomized_partition(seq, begin, end):
    idx = randrange(begin, end)
    seq[idx], seq[end - 1] = seq[end - 1], seq[idx]
    return partition(seq, begin, end)

def partition(seq, begin, end):
    pivot = seq[end - 1]
    i = begin
    for j in range(begin, end - 1):
        if seq[j] <= pivot:
            seq[i], seq[j] = seq[j], seq[i]
            i = i + 1
    seq[i], seq[end - 1] = seq[end - 1], seq[i]
    return i


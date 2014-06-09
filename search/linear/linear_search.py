def linear_search(seq, elem):
    for i in range(len(seq)):
        if seq[i] == elem:
            return i
    return len(seq)

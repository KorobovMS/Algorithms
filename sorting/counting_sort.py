# Array A has elements in [0, k]
def counting_sort(A, k):
    B = [0] * len(A)
    C = [0] * (k + 1)
    for x in A:
        C[x] = C[x] + 1
    for i in range(len(C) - 1):
        C[i + 1] = C[i + 1] + C[i]
    for x in reversed(A):
        B[C[x]-1] = x
        C[x] = C[x] - 1
    A[:] = B

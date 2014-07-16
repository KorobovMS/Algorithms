class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, x):
        self.heap.append(x)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            p_idx = self._parent(i)
            self.heap[p_idx], self.heap[i] = self.heap[i], self.heap[p_idx]
            i = p_idx

    def get_maximum(self):
        if len(self.heap) == 0:
            raise Exception('Heap is empty')
        return self.heap[0]

    def pop(self):
        length = len(self.heap)
        m = self.get_maximum()
        self.heap[0] = self.heap[length - 1]
        self.heap.pop()
        self._heapify(0)
        return m

    def _heapify(self, i):
        length = len(self.heap)
        while 2*i + 1 < length:
            swap = i
            if self.heap[2*i + 1] > self.heap[swap]:
                swap = 2*i + 1
            if 2*i + 2 < length and self.heap[2*i + 2] > self.heap[swap]:
                swap = 2*i + 2
            if swap != i:
                self.heap[i], self.heap[swap] = self.heap[swap], self.heap[i]
                i = swap
            else:
                break

    def _parent(self, i):
        return (i - 1) // 2

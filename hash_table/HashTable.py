class HashTable:
    def __init__(self, hash_func=hash, init_size=100):
        self.size = init_size
        self.buckets = [None]*self.size
        self.hash_func = hash_func

    def h(self, key):
        return self.hash_func(key) % self.size

    def insert(self, key, value):
        idx = self.h(key)
        if self.buckets[idx] is None:
            self.buckets[idx] = Node(key, value)
        else:
            new_node = Node(key, value, next=self.buckets[idx])
            self.buckets[idx] = new_node

    def search(self, key):
        idx = self.h(key)
        if self.buckets[idx] is None:
            return None
        p = list_search(self.buckets[idx], key)
        if p is None:
            return None
        return p.value

    def delete(self, key):
        idx = self.h(key)
        if self.buckets[idx] is None:
            return
        new_head = list_delete(self.buckets[idx], key)
        self.buckets[idx] = new_head

class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

def list_search(head, key):
    p = head
    while p != None and p.key != key:
        p = p.next
    return p

def list_delete(head, key):
    if head.key == key:
        return head.next
    p = head
    while p.next != None and p.next.key != key:
        p = p.next
    if p.next != None:
        p.next = p.next.next
    return head




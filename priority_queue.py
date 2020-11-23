# PriorityQueue: An efficient priority queue.
# If you use a binary heap, it'll do most of the work, leaving this
# implementation quite trivial.
# Your implementation should pass the tests in test_priority_queue.py.
# YOUR NAME

from max_heap import MaxHeap

class PriorityQueue:

    def __init__(self):
        self.heap = MaxHeap()

    def enqueue(self, value):
        self.heap.insert(value)

    def dequeue(self):
        return self.heap.delete()

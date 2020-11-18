# NaivePriorityQueue (aka 'ShittyQueue'): A simple but inefficient priority queue.
# Your implementation should pass the tests in test_naive_priority_queue.py.
# YOUR NAME

class NaivePriorityQueue:

    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        element = self.data[0]
        for current_element in self.data:
            if current_element.priority > element.priority:
                element = current_element
        self.data.remove(element)
        return element

# NaivePriorityQueue (aka 'ShittyQueue'): A simple but inefficient priority queue.
# Your implementation should pass the tests in test_naive_priority_queue.py.
# YOUR NAME

class NaivePriorityQueue:

    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        element = self.data[0]
        for current_element in self.data:
            if not hasattr(element, 'priority'):
                element = current_element
            if hasattr(current_element, 'priority'):
                if current_element.priority > element.priority:
                    element = current_element
        if not hasattr(element, 'priority'):
            return None
        self.data.remove(element)
        return element

    def is_empty(self):
        return len(self.data) == 0

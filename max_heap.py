# MaxHeap: A binary 'max' heap.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_max_heap.py.
# YOUR NAME

class MaxHeap:

   def __init__(self):
      self._data = []

   def _size(self):
      return len(self._data)

   def _is_empty(self):
      return self._size() == 0

   def _last_index(self):
      return self._size() - 1

   def _value_at(self, index):
      return self._data[index]

   def _left_child_index(self, index):
      return 2 * index + 1

   def _right_child_index(self, index):
      return 2 * index + 2

   def _parent_index(self, index):
      return round(index / 2 - 0.6)

   def _parent(self, index):
      return self._value_at(self._parent_index(index))

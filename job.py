# Job: A process or task that has a priority.
# Your implementation should pass the tests in test_job.py.
# YOUR NAME

class Job:

    def __init__(self, priority = None, message = None):
        self.priority = priority
        self.message = message

    def __eq__(self, other):
        if not isinstance(other, Job):
            return NotImplemented
        return self.priority == other.priority

    def __lt__(self, other):
        if not isinstance(other, Job):
            return NotImplemented
        return self.priority < other.priority

    def __gt__(self, other):
        if not isinstance(other, Job):
            return NotImplemented
        return self.priority > other.priority

    def __le__(self, other):
        if not isinstance(other, Job):
            return NotImplemented
        return self.priority <= other.priority

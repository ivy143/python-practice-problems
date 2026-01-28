#implement a queue using deque
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Front element:", queue.queue[0])  # Output: Front element: 1
print("Queue size:", queue.size())       # Output: Queue size: 3
print("Dequeued element:", queue.dequeue())  # Output: Dequeued element: 1
print("Queue size after dequeue:", queue.size())  # Output: Queue size after dequeue: 2
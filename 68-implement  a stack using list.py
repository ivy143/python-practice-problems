#implement a stack using list
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Top element:", stack.peek())  # Output: Top element: 3
print("Stack size:", stack.size())   # Output: Stack size: 3
print("Popped element:", stack.pop())  # Output: Popped element: 3
print("Stack size after pop:", stack.size())  # Output: Stack size after pop: 2
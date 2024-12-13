class Stack:
    def __init__(self, items=None, limit=None):
        if items is None:
            items = []  # Initialize with an empty list if no items are passed
        self.items = items
        self.limit = limit  # Set the limit value if provided (or None if not)

    def push(self, item):
        # Only raise an OverflowError if the stack is full (size >= limit)
        if self.limit is not None and len(self.items) >= self.limit:
            raise OverflowError("Stack is full! Cannot push item.")
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack underflow! Cannot pop item, stack is empty.")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty.")
            return None

    def isEmpty(self):
        return len(self.items) == 0  # Returns True if the stack is empty

    def size(self):
        return len(self.items)  # Returns the number of elements in the stack

    def empty(self):
        return self.isEmpty()  # Returns True if the stack is empty, False otherwise

    def full(self):
        # The stack is full if its size is equal to the limit
        if self.limit is None:
            return False  # If no limit is set, the stack is never full
        return len(self.items) >= self.limit  # Returns True if the stack is full

    def search(self, value):
        try:
            # Find the index of the value in the stack, return the distance from the top
            index = self.items.index(value)
            return len(self.items) - 1 - index  # Distance from the top of the stack
        except ValueError:
            return -1  # If value is not found

    def __str__(self):
        return f"Stack(items={self.items}, limit={self.limit})"

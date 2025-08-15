from coding import DynamicArray

class Stack:
    """Stack LIFO based on DynamicArray."""
    def __init__(self, init_capacity=4):
        self._arr = DynamicArray(init_capacity)
    
    def push(self, value) -> None:
        self._arr.append(value)
    
    def pop(self):
        if len(self._arr) == 0:
            raise IndexError("Pop from empty stack")
        return self._arr.pop()
    
    def peek(self):
        if len(self._arr) == 0:
            raise IndexError("Peek from empty stack")
        return self._arr[len(self._arr) - 1]
    
    def __len__(self):
        return len(self._arr)
    
    def is_empty(self):
        return len(self._arr) == 0
    
    def clear(self):
        """Clears stack and returns old elements (from bottom to top)"""
        return self._arr.clear()
    
    def __repr__(self):
        return f"Stack([{repr(self._arr)}])"
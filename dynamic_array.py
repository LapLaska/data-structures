from typing import Iterable, Any

class DynamicArray:
    def __init__(self, init_capacity: int = 4):
        if init_capacity < 1:
            raise ValueError('too small capacity ( must be >= 1)')
        self._initial_capacity = init_capacity
        self._capacity = init_capacity
        self._size = 0
        self._data = [None] * self._capacity # boofer
        
    def __len__(self):
        return self._size
    
    def __repr__(self):
        visible = ", ".join(repr(self._data[i]) for i in range(self._size))
        return f"DynamicArray([{visible}])"
        
    def _resize(self, new_capacity: int):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity
        
    def append(self, value):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1
        
    def extend(self, iterable: Iterable[Any]):
        for elem in iterable:
            if self._size == self._capacity:
                self._resize(self._capacity * 2)
            self._data[self._size] = elem
            self._size += 1
            
    def _shrink(self):
        if 0 < self._size <= self._capacity // 4:
            self._resize(max(self._initial_capacity, self._capacity // 2))
        
    def pop(self, index=None):
        if self._size == 0:
            raise IndexError('Pop from an empty array')
        if index is None:
            index = self._size - 1
        if not isinstance(index, int):
            raise ValueError("Index must be int")
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        val = self._data[index]
        for i in range(index, self._size-1):
            self._data[i] = self._data[i+1]
        self._data[self._size - 1] = None
        self._size -= 1
        self._shrink()
        return val
        
    def clear(self):
        # capture a copy of the current logical contents (without None's)
        old_data = tuple(self._data[i] for i in range(self._size))
        # reset to initial capacity and empty state
        self._capacity = self._initial_capacity
        self._data = [None] * self._capacity
        self._size = 0
        return old_data
    
    def __contains__(self, item):
        # return item in self._data[:self._size] is less eficcient
        # when working with huge data amount because of extra-copying
        for i in range(self._size):
            if self._data[i] == item:
                return True
        return False
        # this works better with huge amount of data (without extra-copy)
    
    def index(self, value):
        for i in range(self._size):
            if self._data[i] == value:
                return i
    
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be int")
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        return self._data[index]
    
    def __setitem__(self, index, item):
        if not isinstance(index, int):
            raise TypeError("Index must be int")
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        self._data[index] = item
    
    def count(self, value):
        counter = 0
        for i in range(self._size):
            if self._data[i] == value:
                counter += 1
        return counter

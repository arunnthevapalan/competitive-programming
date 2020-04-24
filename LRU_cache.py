'''
Problem 24 - 24/04/2020
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
      get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
      put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, 
      it should invalidate the least recently used item before inserting a new item.
      The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?
'''

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  # To keep this pair fresh, move to end of OrderedDict
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False) # last=True, LIFO; last=False, FIFO We want to remove in FIFO fashion. 
        else:
            self.cache.move_to_end(key) # To keep this pair fresh, move to end of OrderedDict
        self.cache[key] = value

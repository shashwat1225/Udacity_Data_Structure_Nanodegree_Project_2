
from collections import OrderedDict as od
class LRU_Cache(object):
    def __init__(self, capacity):
            self.capacity = capacity
            self.cache = od()
            
            # Initialize class variables
            pass
    
    def get(self, key):
            if key in self.cache:
                self.cache.move_to_end(key)
                return self.cache[key]
            else:
                return -1
            # Retrieve item from provided key. Return -1 if nonexistent. 
            pass
    
    def set(self, key, value):
            self.cache[key] = value
            self.cache.move_to_end(key)
            if len(self.cache)>self.capacity:
                self.cache.popitem(last = False)
            # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
            
            pass
#Test Cases
cache_object = LRU_Cache(5)

cache_object.set(1, 1);
cache_object.set(2, 2);
cache_object.set(3, 3);
cache_object.set(4, 4);


print(cache_object.get(1))       # returns 1
print(cache_object.get(2))       # returns 2
print(cache_object.get(9))      # returns -1 because 9 is not present in the cache

cache_object.set(5, 5) 
cache_object.set(6, 6)

print(cache_object.get(3))# returns -1 because the cache reached it's capacity and 3 was the least recently used entry


cache_object = LRU_Cache(0)
cache_object.set(5, 5) 
cache_object.set(6, 6)

print(cache_object.get(2))

cache_object = LRU_Cache(-1)
cache_object.set(5, 5) 
cache_object.set(6, 6)

print(cache_object.get(9))

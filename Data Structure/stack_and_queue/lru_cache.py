import time

# node class
class Node:
    def __init__(self, key, value, ttl_ms):
        self.key = key
        self.value = value
        # TTL calculation is correct
        self.expiry = time.time() + (ttl_ms/1000)
        self.prev  = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        # This will hold only the real nodes (not head/tail)
        self.cache = {} 
 
        # Create dummy head (LRU Side) and dummy tail (MRU) side
        self.head = Node(0, 0, 0)
        self.tail = Node(0, 0, 0)

        # connect them
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # We don't need 'self' as an argument here, but Python adds it implicitly
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add(self, node):
        prev_node = self.tail.prev
        
        # Connect new node to previous node (prev_node is the current MRU)
        node.prev = prev_node
        prev_node.next = node

        # connect new node to tail
        node.next = self.tail
        self.tail.prev = node


    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
        
            # TTL check
            if time.time() > node.expiry:
                # Expired: remove and delete
                self._remove(node)
                del self.cache[key]
                return None
            
            # If valid, make it MRU
            self._remove(node)
            self._add(node)
            return node.value
            
        return None # Key not found

    def set(self, key, value, ttl_ms):
        # 1. If key exists, update value/TTL and make it MRU
        if key in self.cache:
            self._remove(self.cache[key]) # Remove old position
        
        # 2. Create new node (or use the existing key)
        new_node = Node(key, value, ttl_ms)
        self._add(new_node)
        self.cache[key] = new_node
        

        # 3. Check capacity - only count items in the cache dict
        # The head/tail dummies are not counted.
        if len(self.cache) > self.capacity:
            # Evict the LRU (the node right after the dummy head)
            lru_node = self.head.next
            self._remove(lru_node)
            del self.cache[lru_node.key]
            
if __name__ == "__main__":
    # Initialize
    cache = LRUCache(capacity=2)
    
    print("--- Test 1: Standard LRU ---")
    cache.set("A", "ValueA", 10000) # Big TTL
    cache.set("B", "ValueB", 10000)
    print(f"Get A: {cache.get('A')}") # Returns ValueA, A is now MRU
    
    cache.set("C", "ValueC", 10000) # Capacity full! B is LRU, should be evicted.
    
    print(f"Get B (should be None): {cache.get('B')}") 
    print(f"Get C: {cache.get('C')}")
    
    print("\n--- Test 2: TTL Expiration ---")
    cache.set("Quick", "FastData", 500) # Lives for 500ms (0.5s)
    print(f"Immediate Get: {cache.get('Quick')}") # Should be FastData
    
    print("Sleeping for 0.6 seconds...")
    time.sleep(0.6)
    
    print(f"Delayed Get (should be None): {cache.get('Quick')}")
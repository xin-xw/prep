"""
Understand: 
* LRU: Least recently used
- We're to implement class LRUCache where we can instantiate object LRUCache with a capacity parameter LRUCache(int capacity).
- The class should support these operations:
    1. int get(int key): Return the value that corresponds to the key if the key exists
        - There needs to be a mapping (key: value) inside our cache
        - Hash Map?
        * Return -1 if the key does not exist
    2. void put(int key, int value): Update the value of the key if the key exists, if the key does not exist, make sure to add the key:value pair into our cache.
        - Key exists
            - Update value
        - Key does not exist
            - Add key:value pair into our cache
                - If new key:value pair > capacity of cache, remove LRU key

* This problem has 2 asks:
1. Provided a key, return its value in O(1) -> Hash Map
2. Track recency/Validate and verify which key is least recently used 
    - Using a list here to track recency will result in O(n) time
    * If we were to use a normal list, the T.C. of the operations: scanning, removing, and appending would be O(n) time. To improve it, we can instead use a linked list, and use a hash map to map the keys to a node instead. By doing so, the node itself will reveal the position of each and every node and thus reducing the time complexities to O(1).

Match:
- Hash Map, Doubly Linked List

Plan:
1. Let's create a class for the Node and keep track of the key, value, prev, next.

class Node:
    def __init__(self, key, value, prev, next)
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
    
2. Now our LRUCache class will serve as an actual implementation for the DLL that we were describing.

"""
class Node:
    def __init__(self, key, value, prev_node=None, next_node=None):
        self.key = key
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node("dummy", "dummy")
        self.tail = Node("dummy", "dummy")
        self.head.next_node = self.tail
        self.tail.prev_node = self.head
        self.dic = {} # dictionary to hold our mappings of key : node
        
    def _remove(self, node):
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node
        
        # 1<->2<->3
        # 1<->3

    def _add(self, node):
        # add node to our linked list in front of tail (to indicate most recently used)
        prev_tail = self.tail.prev_node
        prev_tail.next_node = node
        node.prev_node = prev_tail
        node.next_node = self.tail
        self.tail.prev_node = node


    def get(self, key: int) -> int:
        
        if key not in self.dic:
            return -1
        fetched_node = self.dic[key]
        # make this most recently used
        # we can do this by removing and then adding it to the end again right?
        self._remove(fetched_node)
        self._add(fetched_node)
        return fetched_node.value
            

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            fetched_node = self.dic[key]
            fetched_node.value = value
            self._remove(fetched_node)
            self._add(fetched_node)
        else:
            # if key does not exist, need to check capacity
            if len(self.dic) == self.capacity:
                # remove least recently used node 
                key_to_remove = self.head.next_node.key
                self._remove(self.head.next_node) # we know it to be the head.next (dummy)
                del self.dic[key_to_remove]

    
            # now we can actually add the new node, knowing that our cache is not at capacity
            new_node = Node(key, value)
            self.dic[key] = new_node
            self._add(new_node)
            


        

https://leetcode.com/problems/all-oone-data-structure/

432. All O`one Data Structure

Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"

https://leetcode.com/problems/all-oone-data-structure/solutions/91428/python-solution-with-detailed-comments/

from collections import defaultdict
class Node(object):
    def __init__(self):
        self.key_set = set([])
        self.prev, self.nxt = None, None 

    def add_key(self, key):
        self.key_set.add(key)

    def remove_key(self, key):
        self.key_set.remove(key)        

    def get_any_key(self):
        if self.key_set:
            result = self.key_set.pop()
            self.add_key(result)
            return result
        else:
            return None
    
    def count(self):
        return len(self.key_set)

    def is_empty(self):
        return len(self.key_set) == 0


class DoubleLinkedList(object):
    def __init__(self):
        self.head_node, self.tail_node = Node(), Node()
        self.head_node.nxt, self.tail_node.prev = self.tail_node, self.head_node
        return

    def insert_after(self, x):
        node, temp = Node(), x.nxt
        x.nxt, node.prev = node, x
        node.nxt, temp.prev = temp, node
        return node
    
    def insert_before(self, x):
        return self.insert_after(x.prev)

    def remove(self, x):
        prev_node = x.prev
        prev_node.nxt, x.nxt.prev = x.nxt, prev_node
        return

    def get_head(self):
        return self.head_node.nxt
    
    def get_tail(self):
        return self.tail_node.prev

    def get_sentinel_head(self):
        return self.head_node

    def get_sentinel_tail(self):
        return self.tail_node
    
class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dll, self.key_counter = DoubleLinkedList(), defaultdict(int)
        self.node_freq = {0:self.dll.get_sentinel_head()}

    def _rmv_key_pf_node(self, pf, key):
        node = self.node_freq[pf]
        node.remove_key(key)
        if node.is_empty():
            self.dll.remove(node)
            self.node_freq.pop(pf)
        return

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        self.key_counter[key] += 1
        cf, pf = self.key_counter[key], self.key_counter[key]-1
        if cf not in self.node_freq:
            # No need to test if pf = 0 since frequency zero points to sentinel node
            self.node_freq[cf] = self.dll.insert_after(self.node_freq[pf])
        self.node_freq[cf].add_key(key)
        if pf > 0:
            self._rmv_key_pf_node(pf, key)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.key_counter:
            self.key_counter[key] -= 1
            cf, pf = self.key_counter[key], self.key_counter[key]+1
            if self.key_counter[key] == 0:
                self.key_counter.pop(key)
            if cf != 0:
                if cf not in self.node_freq:
                    self.node_freq[cf] = self.dll.insert_before(self.node_freq[pf])
                self.node_freq[cf].add_key(key)
            self._rmv_key_pf_node(pf, key)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return self.dll.get_tail().get_any_key() if self.dll.get_tail().count() > 0 else ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return self.dll.get_head().get_any_key() if self.dll.get_tail().count() > 0 else ""


class Node:
    # def __init__(self):
    #     self.next = NULL
    #     self.prev = NULL
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.m = {}
        self.size = 0
        self.cap = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        curr = self.m[key]

        n, p = curr.next, curr.prev
        n.prev = p
        p.next = n

        curr.next = self.head.next
        curr.prev = self.head

        self.head.next.prev = curr
        self.head.next = curr

        return self.m[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.m[key].val = value
            self.get(key)
            return
        self.size+=1
        if self.size > self.cap:
            self.size = self.cap
            k = self.tail.prev.key
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            self.m.pop(k)
        entry = Node(key, value)
        entry.next = self.head.next
        entry.prev = self.head
        self.head.next.prev = entry
        self.head.next = entry

        self.m[key] = entry
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

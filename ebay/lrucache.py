from collections import deque


class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class GoodLRUCache:
    """
    Implementing LRU cache using a dictionary and doubly-linked list.

    ------  -->  ------------  -->  ------------  -->  ------
     HEAD         Node(1, 1)         Node(2, 2)         TAIL
    ------  <--  ------------  <--  ------------  <--  ------
                      :                 :
    dict {            1         ,       2               }

    Performance:
        put() -> O(1)
        get() -> O(1)
    """
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.prev = self.tail
        self.tail.next = self.head

        self._dict = {}
        self.capacity = capacity

    def _add_to_head(self, key: int, value: int):
        node = Node(key, value)
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node
        node.next = self.head

        self._dict[key] = node

    def _remove_from_tail(self):
        popped_key = self.tail.next.key

        self.tail.next.prev = None
        self.tail.next = self.tail.next.next
        self.tail.next.prev.next = None
        self.tail.next.prev = self.tail

        self._dict.pop(popped_key)

    def _remove_from_middle(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

        self._dict.pop(node.key)

    def get(self, key: int) -> int:
        if self._dict.get(key):
            node = self._dict.get(key)
            self._remove_from_middle(node)
            self._add_to_head(node.key, node.value)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self._dict) == self.capacity:
            self._remove_from_tail()

        self._add_to_head(key, value)


class CrappyLRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._queue = deque(maxlen=capacity)
        self._dict = {}

    def get(self, key: int) -> int:
        if self._queue:
            indices = [idx for i, idx in zip(self._queue, range(len(self._queue))) if i == key]
            if indices:
                del self._queue[indices[0]]
                self._queue.append(key)
        return self._dict.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self._dict:
            self._dict[key] = value
            indices = [idx for i, idx in zip(self._queue, range(len(self._queue))) if i == key]
            if indices:
                del self._queue[indices[0]]
                self._queue.append(key)
            return
        if len(self._queue) == self.capacity:
            key_popped = self._queue.popleft()
            self._dict.pop(key_popped)
        self._queue.append(key)
        self._dict[key] = value


if __name__=="__main__":
    cache = GoodLRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

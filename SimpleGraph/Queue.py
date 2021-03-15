# https://skillsmart.ru/algo/py-kf32y/ce2fd8a857.html

class _Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class _DummyNode(_Node):
    def __init__(self):
        super().__init__(None)

class Queue:
    def __init__(self):
        self.head = _DummyNode()
        self.tail = _DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def enqueue(self, item):
        node = _Node(item)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.length += 1

    def dequeue(self):
        if self.length:
            val = self.head.next.value # val = out:  head -> first -> second -> ..
            self.head.next = self.head.next.next # head -> new first (previously second) -> ..
            self.head.next.prev = self.head
            self.length -= 1
            return val
        return None

    def size(self):
        return self.length

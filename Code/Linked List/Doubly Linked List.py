class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = self.prev = self

    def __str__(self):
        return str(self.key)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __iter__(self):
        v = self.head
        while v != None:
            yield v
        v = v.next

    def __str__(self):
        return "->".join(str(v) for v in self)

    def __len__(self):
        return self.size

    def splice(self, a, b, x):
        if a == None or b == None or x == None:
            return
        ap = a.prev
        bn = b.next

        ap.next = bn # cut[a..b]
        bn.prev = ap

        xn = x.next
        xn.prev = b # insert [a..b] after x
        b.next = xn
        a.prev = x
        x.next = a

    def search(self, key):
        v = self.head
        while v.next != self.head:
            if v.key == key:
                return v
            v = v.next
        return None

    def remove(self, x):
        if x == None or x == self.head:
            return
        x.prev.next = x.next
        x.next.prev = x.prev

    def popFront(self):
        if self.isEmpty():
            return None
        key = self.head.next.key
        self.remove(self.head.next)
        return key
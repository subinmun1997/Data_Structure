class Node:
    def __int__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.key)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __iter__(self):
        v = self.head
        while v != Node:
            yield v
            v =v.next

    def __str__(self):
        return "->".join(str(v) for v in self)

    def __len__(self):
        return self.size

    def pushFront(self, key, value=None):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pushBack(self, key, value=None):
        new_node = Node(key, value)
        if self.size == 0:
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def popFront(self):
         if self.size == 0:
             return None
         else:
             x = self.head
             key = x.key
             self.head = x.next
             self.size = self.size - 1
             del x
             return key

    def popBack(self):
        if self.size == 0:
            return None
        else:
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if prev == None:
                self.head = None
            else:
                prev.next = tail.next
            key = tail.key
            del tail
            self.size -= 1
            return key

    def search(self, key):
        v = self.head
        while v != None:
            if v.key == key:
                return v
            v = v.next
        return v


class Stack():
    def __init__(self):
        self.items = []
    def push(self, val):
        self.items.append(val)
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty") # ')' 오른쪽이 더 많은 경우 Error
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
            return
    def __len__(self):
        return len(self.items)
    def isEmpty(self):
        return len(self) == 0

s = Stack()
parSeq = "(())"
for p in parSeq:
    if p == '(':
        s.push(p)
    elif p == ')':
        s.pop()
    else:
        print("Not allowed Symbol")


if len(s)>0 : # '(' 왼쪽이 더 많은 경우 Error
    print("false")
else:
    print("true")

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def IsEmpty(self):
        if not self.stack:
            return True
        else:
            return False

    def top(self):
        if self.IsEmpty():
            print("stack에 원소가 없습니다.")
        else:
            print(self.stack[-1])
            print("stack에 원소가 있습니다")

stack = Stack()
print(stack.IsEmpty())
stack.top()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.IsEmpty())
stack.top()

while not stack.IsEmpty():
    print(stack.pop(), end=' ')
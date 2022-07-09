class Stack:
    def __init__(self): #생성자
        self.container = []

    def empty(self): #스택이 비어 있으면 TRUE, 아니면 FALSE 반환하는 함수
        if not self.container:
            return True
        else:
            return False

    def push(self, data): #data를 스택의 맨 위에 삽입하는 함수
        self.container.append(data) 

    def pop(self): #스택의 맨 위에 있는 데이터를 삭제하며 반환하는 함수
        if self.empty():
            return None
        return self.container.pop()

    def peek(self): #스택의 맨 위에 있는 데이터를 반환하는 함수
        if self.empty():
            return None
        return self.container[-1]

s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

while not s.empty():
    print(s.pop(), end=' ')
class Stack():
    def init(self):
        self.stack = []
    def push(self, data): #원소 추가
        self.stack.append(data)
    def pop(self): #원소 삭제
        # n=len(self.stack)
        # self.stack.pop(n-1)
        self.stack.pop()
    def IsEmpty(self): # 스택 확인
        if not self.stack: # not == !
            return True
        else:
            return False
    def top(self):
        if self.IsEmpty():
            print("stack에 원소가 없습니다")
        else:
            print(self.stack[-1])
            print("stack에 원소가 있습니다")

stack = Stack()
print(stack.IsEmpty()) #False
stack.top() #원소 없
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
# print(stack.IsEmpty()) #True
# stack.top() #pop값 반환

while not stack.IsEmpty(): #비어있지 않을 동안
    print(stack.pop(), end=' ')
class Que:
    def init(self):
        self.que = []

    def empty(self): #큐가 비어 있으면 TRUE, 아니면 FALSE 반환하는 함수
        if not self.que:
            return True
        else:
            return False
            
    def full(self):
        n = len(self.que)
        if not self.que[n-1]:
            return False
        else:
            return True

    def enqueue(self,data):
        self.que.append(data)

    def dequeue(self):
        if self.empty():
            return None
        self.que.pop[0]

    def peek(self):
        if self.empty():
            return None
        return self.container[0]

    
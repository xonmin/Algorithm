class Stack(object):

    def __init__(self):
        self.container = list()

    def empty(self):
        if not self.container:
            return True
        return False

    def push(self, item):
        self.container.append(item)

    def pop(self):
        if not self.empty():
            return self.container.pop()

    # stack_out 에 아무것도 없는 상황에서 pop을 수행하려 할 때 stack_in의 값들을 모두 stack_out 에 넣어주어 나오게


class Queue:
    def __init__(self):
        self.first = Stack()
        self.second = Stack()

    def empty(self):
        if self.first.empty() and self.second.empty():
            return True
        return False

    def enqueue(self, item):
        self.first.push(item)

    def dequeue(self):
        if self.empty():
            print("empty!")
            return None
        if self.second.empty():
            # 첫번째 잇는 거 다 넣기
            while not self.first.empty():
                self.second.push(self.first.pop())
        return self.second.pop()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
#
# for i in q.first.container:
#     print(i)
q.enqueue(4)
q.enqueue(5)
#
while not q.empty():
    print(q.dequeue())
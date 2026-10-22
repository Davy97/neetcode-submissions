class MyQueue:

    def __init__(self):
        self.s = []
        self.d = []

    def push(self, x: int) -> None:
        while self.d:
            self.s.append(self.d.pop())
        self.s.append(x)

    def pop(self) -> int:
        while self.s:
            self.d.append(self.s.pop())
        return self.d.pop()
        

    def peek(self) -> int:
        while self.s:
            self.d.append(self.s.pop())
        return self.d[-1]

    def empty(self) -> bool:
        return len(self.s) + len(self.d) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
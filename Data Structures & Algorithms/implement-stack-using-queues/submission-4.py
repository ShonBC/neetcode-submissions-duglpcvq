from collections import deque


class MyStack:

    def __init__(self):
        self.que = None

    def push(self, x: int) -> None:
        self.que = deque([x, self.que])

    def pop(self) -> int:
        top = self.que.popleft()
        self.que = self.que.popleft()
        return top

    def top(self) -> int:
        return self.que[0]

    def empty(self) -> bool:
        if self.que:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedStack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, x):
        self._top = Node(x, self._top)
        self._size += 1

    def pop(self):
        if self._top is None:
            print("栈为空")
            return
        else:
            res = self._top.data
            self._top = self._top.next
            self._size -= 1
            return res

    def top(self):
        if self._top is None:
            print("栈为空")
            return
        else:
            res = self._top.data
            return res

if __name__ == "__main__":
    s = LinkedStack()
    for i in range(10):
        s.push(i)

    while s._top:
        print(s.pop())



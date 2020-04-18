class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


    def __str__(self):
        return "<Node %r>" % self.data




if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("a")

    print(a)
    print(a.next)
    print(f)
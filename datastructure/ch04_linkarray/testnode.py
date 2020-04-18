from node import Node


if __name__ == "__main__":
    head = None

    for count in range(6, 0, -1):  # for count in range(1, 7)
        head = Node(count, head)

    while head:
        print(head)
        head = head.next
from node import Node

class SingleLink(object):
    def __init__(self, datas = []):
        if datas:
            # self.root = Node(datas[0])
            # current_node = self.root
            # for item in datas[1:]:
            #     tmp  = Node(item)
            self.root = Node(datas[-1])   # 从后往前建立单链表
            for item in datas[:-1][::-1]:
                self.root = Node(item, self.root)
        else:
            self.root = None


    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return
        head = self.root
        while head.next:   # 找到需要插入的位置
            head = head.next
        head.next = Node(data)


    def search(self, data):
        head = self.root
        while head and head.data != data:
            head = head.next
        # if head:  # 找到
        #     return True
        # else:  # 没有找到
        #     return False
        return head  # 如果head为None,说明没有找到，否则找到了

    def delete(self, data):
        pass

if __name__ == "__main__":
    link = SingleLink(datas=[1,2,3,4,5])

    head = link.search(3)
    print(head)
    exit(-1)

    link.insert(6)
    while link.root:
        print(link.root)
        link.root = link.root.next
    print(link.root)
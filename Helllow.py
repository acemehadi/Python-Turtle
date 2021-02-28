class Node:
    def __init__(self, vaule):
        self.next = None
        self.prev = None
        self.vaule = vaule


class DuoLinkListed:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, vaule):
        node = Node(vaule)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.head.next=node
            node.prev=self.head
            self.tail=node
            self.size+=2

    def __str__(self):
        value=[]
        Node=self.head
        while node is not None:
            value.append(node.vaule)
            node=node.next
        return 

my_list=DuoLinkListed()
my_list.add(1)
my_list.add(6)
my_list.add(2)
print(my_list)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


def push(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node


def insertafter(self, prev_node, new_data):
    if prev_node is None:
        return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node


def append(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
        self.head = new_node
    else:
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


list = linkedlist()
list.head = Node(1)
second = Node(2)
third = Node(3)
list.head.next = second
second.next = third

append(list, 5)
list.printList()

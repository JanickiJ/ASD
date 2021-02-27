class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def printList(self):
    temp = self.head
    while temp:
        print(temp.data)
        temp = temp.next


def append(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
        self.head = new_node
    else:
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


def listlen(self):
    counter = 0
    temp = self.head
    while temp:
        counter += 1
        temp = temp.next
    return counter


def Bubblesort(self):
    temp = self.head
    for i in range(listlen(self) - 1):
        temp1 = temp
        for n in range(i, listlen(self) - 1):
            if temp1.next.data < temp1.data:
                temp1.next.data, temp1.data = temp1.data, temp1.next.data
            temp1 = temp1.next
    temp = temp.next


def Bubblesort(self):
    temp = self.head
    while temp.next:
        temp1 = temp
        while temp1.next:
            if temp1.next.data < temp1.data:
                temp1.next.data, temp1.data = temp1.data, temp1.next.data
            temp1 = temp1.next
        temp = temp.next


lista = LinkedList()
append(lista, 1)
append(lista, 11)
append(lista, 5)
append(lista, 23)
append(lista, 2)
append(lista, 6)
append(lista, 4)
append(lista, 11)
printList(lista)
Bubblesort(lista)
printList(lista)

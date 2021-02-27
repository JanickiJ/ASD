import math

class Node:
    def __init__(self,key,val):
        self.next = None
        self.key = key
        self.val = val

def hashfun(key, n):
    a = (math.sqrt(5) - 1) / 2
    length = len(key)
    sum = 0
    for i in range(length):
        sum += ord(key[i])
    idx = int(n * ((sum * a) % 1))
    return idx


class Dictionary:
    def __init__(self,n):
        self.tab = [Node(None,None)] * n
        self.size = n
    def insert(self, key,val):
        idx = hashfun(key, self.size)
        new = Node(key, val)
        new.next = self.tab[idx].next
        self.tab[idx].next = new
    def find(self, key):
        idx = hashfun(key, self.size)
        tmp = self.tab[idx].next
        while tmp is not None and tmp.key != key:
            tmp = tmp.next
        if tmp is None:
            return tmp
        else:
            return tmp.val
    def remove(self, key):
        idx = hashfun(key, self.size)
        tmp = self.tab[idx].next
        prev = self.tab[idx]

        while tmp is not None and tmp.key != key:
            tmp = tmp.next
            prev = prev.next
        if tmp.key == key:
            prev.next = tmp.next

d=Dictionary(1)
d.insert('a',1)
d.insert('b',2)
d.insert('c',3)
d.insert('d',4)
d.insert('e',5)
d.insert('f',1)
print(d.find('f'))
d.remove('f')
print(d.find('a'))




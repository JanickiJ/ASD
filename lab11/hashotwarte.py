import math


class Node:
    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.status = 0


def hashfun(key, n):
    a = (math.sqrt(5) - 1) / 2
    l = len(key)
    sum = 0
    for i in range(l):
        sum += ord(key[i])
    idx = int(n * ((sum * a) % 1))
    return idx


class Dictionary:
    def __init__(self, n):
        self.tab = [Node(None, None)] * n

    def insert(self, key, data):
        n = len(self.tab)
        idx = hashfun(key, n)
        new = Node(key, data)
        new.status = 2
        x = idx
        while self.tab[idx % n].status == 2:
            idx += 1
            x -= 1
            if x == 0:
                return
        self.tab[idx % n] = new

    def find(self, key):
        n = len(self.tab)
        idx = hashfun(key, n)
        x = n
        while self.tab[idx % n].status != 0 and x != 0:
            if self.tab[idx % n].key == key and self.tab[idx % n].status != 1:
                return self.tab[idx % n].data
            idx += 1
            x -= 1
        return None

    def remove(self, key):
        n = len(self.tab)
        idx = hashfun(key, len(self.tab))
        x = n
        while self.tab[idx % n].status != 0 and x != 0:

            if self.tab[idx % n].key == key:
                self.tab[idx % n].status = 1
                return

            idx += 1
            x -= 1


d = Dictionary(4)
d.insert('a', 1)
d.insert('b', 2)
# d.insert('c',3)
# d.insert('d',4)
d.insert('e', 1)
d.insert('f', 1)
print(d.tab[0].data, d.tab[1].data, d.tab[2].data, d.tab[3].data)
print(d.find('e'))
d.remove('e')
print(d.find('e'))
d.insert('e', 2)

#hash na liczbach

import math


class Node:
    def __init__(self, key):
        self.key = key
        self.status = 0


def hashfun(key, n):
    a = (math.sqrt(5) - 1) / 2
    idx = int(n * ((key * a) % 1))
    return idx


class Dictionary:
    def __init__(self, n):
        self.tab = [Node(None)] * n

    def insert(self, key):
        n = len(self.tab)
        idx = hashfun(key, n)
        new = Node(key)
        new.status = 2
        x = idx
        while self.tab[idx % n].status == 2:
            idx += 1
            x -= 1
            if x == 0:
                return
        self.tab[idx % n] = new

    def find(self, key):
        n = len(self.tab)
        idx = hashfun(key, n)
        x = n
        while self.tab[idx % n].status != 0 and x != 0:
            if self.tab[idx % n].key == key and self.tab[idx % n].status != 1:
                return self.tab[idx % n].key
            idx += 1
            x -= 1
        return None

    def remove(self, key):
        n = len(self.tab)
        idx = hashfun(key, len(self.tab))
        x = n
        while self.tab[idx % n].status != 0 and x != 0:

            if self.tab[idx % n].key == key:
                self.tab[idx % n].status = 1
                return

            idx += 1
            x -= 1

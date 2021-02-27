import math


class Node:
    def __init__(self, key):
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

def hashfunnum(key, n):
    a = (math.sqrt(5) - 1) / 2
    idx = int(n * ((key * a) % 1))
    return idx


class Dictionary:
    def __init__(self, n):
        self.tab = [Node(None)] * n

    def insert(self, key):
        n = len(self.tab)
        idx = hashfunnum(key, n)
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
        idx = hashfunnum(key, n)
        x = n
        while self.tab[idx % n].status != 0 and x != 0:
            if self.tab[idx % n].key == key and self.tab[idx % n].status != 1:
                return self.tab[idx % n].key
            idx += 1
            x -= 1
        return None

    def remove(self, key):
        n = len(self.tab)
        idx = hashfunnum(key, len(self.tab))
        x = n
        while self.tab[idx % n].status != 0 and x != 0:

            if self.tab[idx % n].key == key:
                self.tab[idx % n].status = 1
                return

            idx += 1
            x -= 1


def sum(arr, sum):
    n = len(arr)
    d = Dictionary(n)
    for i in range(n):
        if d.find(sum - arr[i]):
            return True
        else:
            d.insert(arr[i])
    return False

arr = [1,10,23,454,234,123,-76,34,54]
print(sum(arr,0))
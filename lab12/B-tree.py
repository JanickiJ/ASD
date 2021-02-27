class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key
        self.parent = None

class V:
    def __init__(self):
        self.tab = []
    def addtoV(self, key):
        self.tab.append(Node(key))
        self.tab.sort()

class Btree:
    def __init__(self):
        self.root = V()
    def insert(self, key):

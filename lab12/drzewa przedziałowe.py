class Node:
    def __init__(self, key):
        self.parent = None
        self.key = key
        self.right = None
        self.left = None
        self.start = float('-inf')
        self.end = float('inf')
        self.intervals = []

    def succ(self):
        tmp=self
        if tmp.right is not None:
            tmp = tmp.right
            while tmp.left:
                tmp = tmp.left
            return tmp

        parent = tmp.parent
        while parent and parent.left != tmp:
            tmp = parent
            parent = parent.parent
        return parent


    def pred(self):
        tmp = self
        if tmp.left is not None:
            tmp = tmp.left
            while tmp.right:
                tmp = tmp.right
            return tmp

        parent = tmp.parent
        while parent and parent.right != tmp:
            tmp = parent
            parent = parent.parent
        return parent

    def set(self):
        if self.pred():
            self.start = self.pred().key
        if self.succ():
            self.end = self.succ().key

    def makeend(self):
        self.set()
        self.left = Node(None)
        self.right = Node(None)
        self.left.parent = self
        self.right.parent = self
        self.left.set()
        self.right.set()

class Intervaltree:
    def __init__(self):
        self.root = None

    def find(self, key):
        tmp = self.root
        while tmp is not None and tmp.key is not None:
            if tmp.key == key:
                return tmp
            elif key > tmp.key:
                tmp = tmp.right
            else:
                tmp = tmp.left
        return None

    def insertBST(self, key):
        new = Node(key)

        if self.root is None:
            self.root = new
            self.root.makeend()
            return

        tmp = self.root
        parent = None
        while tmp is not None and tmp.key is not None:
            parent = tmp
            if key < tmp.key:
                tmp = tmp.left
            else:
                tmp = tmp.right
        new.parent = parent
        if key < parent.key:
            parent.left = new
        else:
            parent.right = new
        new.makeend()
    def recuaddInterval(self, a, b, node):
        if a <= node.start and b >= node.end:
            node.intervals.append((a,b))
        else:
            if a < node.key and node.left is not None:
                self.recuaddInterval(a, b, node.left)
            if b > node.key and node.right is not None:
                self.recuaddInterval(a, b, node.right)

    def insert(self, a, b):
        if self.find(a) is None:
            self.insertBST(a)
        if self.find(b) is None:
            self.insertBST(b)

        self.recuaddInterval(a, b, self.root)

    def recudelInterval(self, a, b, node):
        if a <= node.start and b >= node.end:
            node.intervals.remove((a,b))
        else:
            if a < node.key and node.left is not None:
                self.recudelInterval(a, b, node.left)
            if b > node.key and node.right is not None:
                self.recudelInterval(a, b, node.right)

    def remove(self, a,b):
        self.recudelInterval(a, b, self.root)

    def query(self, key):
        self.queryreku(self.root, key)

    def queryreku(self, root, key):
        if root is None:
            return
        if root.key is not None:
            if key < root.key:
                self.queryreku(root.left, key)
            elif key > root.key:
                self.queryreku(root.right, key)
            else:
                self.queryreku(root.left, key)
                self.queryreku(root.right, key)
        if len(root.intervals) != 0:
            print(root.intervals)

    def printBST(self, root):
        if root:
            self.printBST(root.left)
            print(root.key)
            for i in range(len(root.intervals)):
                print(root.intervals[i])

            self.printBST(root.right)


a = Intervaltree()
a.insertBST(5)
a.insertBST(3)
a.insertBST(1)
a.insertBST(4)
a.insertBST(7)
a.insertBST(6)
a.insertBST(8)
a.insert(7,8)
a.insert(3,5)
a.insert(1,5)
a.insert(1,6)
a.query(1)
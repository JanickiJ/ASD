class Node:
    def __init__(self, key, val):
        self.parent = None
        self.key = key
        self.val = val
        self.right = None
        self.left = None


class Dictionary:
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        new = Node(key, val)

        if self.root is None:
            self.root = new
            return

        tmp = self.root
        parent = None
        while tmp is not None:
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

    def find(self, key):
        tmp = self.root
        while tmp is not None:
            if tmp.key == key:
                return tmp
            elif key > tmp.key:
                tmp = tmp.right
            else:
                tmp = tmp.left
        return None

    def min(self):
        tmp = self.root
        while tmp is not None and tmp.left is not None:
            tmp = tmp.left
        return tmp

    def max(self):
        tmp = self.root
        while tmp is not None and tmp.right is not None:
            tmp = tmp.right
        return tmp

    def succ(self, key):

        tmp = self.find(key)
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

    def pred(self, key):
        tmp = self.find(key)

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

    def remove(self, key):
        tmp = self.find(key)

        if tmp.left is None or tmp.right is None:
            y = tmp
        else:
            y = self.succ(tmp.key)

        if y.left:
            x = y.left
        else:
            x = y.right

        if x:
            x.parent = y.parent
        if y.parent is None:
            self.root = x
        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x

        if y != tmp:
            tmp.key = y.key

    def printBST(self, root):
        if root:
            self.printBST(root.left)
            print(root.key)
            self.printBST(root.right)


root = Dictionary()
root.insert(30, 'a')
root.insert(20, 'b')
root.insert(40, 'c')
root.insert(50, 'd')
root.insert(60, 'e')
root.insert(70, 'f')
root.insert(80, 'g')
root.insert(10, 'h')

print(root.pred(30).key)

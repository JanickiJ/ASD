class Node:
    def __init__(self, key):
        self.parent = None
        self.key = key
        self.right = None
        self.left = None
        self.start = float('-inf')
        self.end = float('inf')

class Dictionary:
    def __init__(self,tab):
        self.tab=tab
        for i in range(len(tab)):
            self.tab[i] = Node(tab[i])
            self.tab[i].start = tab[i]
            self.tab[i].end = tab[i]
        self.root = self.maketree(self.tab)

    def maketree(self,tab):
        n=len(tab)
        if n == 1:
            return tab[0]
        if n >= 2:
            newTab = []

            for i in range(0, n, 2):
                new = Node(None)
                new.left = tab[i]
                tab[i].parent = new
                new.key = new.left.key
                if i+1<n:
                    tab[i + 1].parent = new
                    new.right = tab[i + 1]
                    new.key += new.right.key
                newTab.append(new)

            return self.maketree(newTab)
    def change(self, idx, key):
        changed = self.tab[idx]
        diff = key - changed.key
        self.tab[idx].key = key

        while changed.parent:
            changed=changed.parent
            changed.key += diff


    def printBST(self, root):
        if root:
            self.printBST(root.left)
            print(root.key)
            self.printBST(root.right)



T=[1,7,2]
A = Dictionary(T)
A.change(2,4)
A.printBST(A.root)
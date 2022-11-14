class Tree:
    def __init__(self, value = None):

        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value == None:
            self.value = value
        else:
            self.insertIntoTree(value)

    def insertIntoTree(self,value):
        if value < self.value:
            self.insertLeft(value)    
        elif value > self.value:
            self.insertRight(value)

    def insertLeft(self, value):
        if self.left is None:
            self.left = Tree(value)
        else:
            self.left.insert(value)

    def insertRight(self, value):
        if self.right is None:
            self.right = Tree(value)
        else:
            self.right.insert(value)

    def printValues(self):
        if self.left:
            self.left.printValues()
        print(self.value)
        if self.right:
            self.right.printValues()

tree = Tree()
tree.insert(19)
tree.insert(24)
tree.insert(5)
tree.insert(21)
tree.printValues()
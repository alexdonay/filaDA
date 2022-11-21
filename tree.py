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
        if self.left is not None:
            self.left.insert(value)
        else:
            self.left = Tree(value)

    def insertRight(self, value):
        if self.right is not None:
            self.right.insert(value)
        else:
            self.right = Tree(value)
        
    def printValues(self):
        if self.left:
            self.left.printValues()
        print(self.value)
        if self.right:
            self.right.printValues()

    def find(self, value) -> int:
        if self.left:
            self.left.find(value)
        if self.right:
            self.right.find(value)
        if self.value == value:
            print(value)
        return self.value
tree = Tree()
tree.insert(19)
tree.insert(24)
tree.insert(5)
tree.insert(21)
print(tree.find(21))


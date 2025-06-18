class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, key):
        if key < self.value: # Checks if key is lesser than parent node
            if self.left is None: # Checks if the child is empty/None
                self.left = TreeNode(key)
            else:
                self.left.insert(key) # Continues traversing deeper until it finds a none and then inserts - recursion
        elif key > self.value: # Checks if key is greater than the parent node
            if self.right is None:
                self.right = TreeNode(key)
            else:
                self.right.insert(key)


    def find(self, key):
        if key < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(key)

        elif key > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(key)

        else:
            return True

    def preorder_traversal(self): # Prints a node when you visit it for the first time
        print(self.value)

        if self.left is not None:
            self.left.preorder_traversal()

        if self.right is not None:
            self.right.preorder_traversal()

    def inorder_traversal(self): # Prints a node the 2nd time its traversed
        if self.left is not None:
            self.left.inorder_traversal() # Recursive call to the bottom of the tree

        print(self.value) # prints after second traversal of a node

        if self.right is not None:
            self.right.inorder_traversal() # Recursive call to the bottom of the tree




    def postorder_traversal(self): # Prints a node after the last visit
        if self.left is not None:
            self.left.postorder_traversal()


        if self.right is not None:
            self.right.postorder_traversal()

        print(self.value)

if __name__ == "__main__":
    tree = TreeNode(10)

    tree.insert(5)
    tree.insert(3)
    tree.insert(4)
    tree.insert(11)
    tree.insert(12)
    tree.insert(13)
    tree.insert(51)
    tree.insert(69)

    tree.preorder_traversal()
    print("\n")

    tree.inorder_traversal()
    print("\n")

    tree.postorder_traversal()

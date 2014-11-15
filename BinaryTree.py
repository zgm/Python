
class TreeNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root==None:
            root = TreeNode(key)
        else:
            if key<root.key:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root
    
    def show(self, root, deep):
        if root==None:
            return
        self.show(root.left,deep+1)
        for i in range(deep):
            print ' ',
        print root.key
        self.show(root.right,deep+1)


if __name__ == '__main__':
    tree = Tree()
    tree.root = tree.insert(tree.root,6)
    #tree.show(tree.root)
    tree.insert(tree.root,3)
    tree.insert(tree.root,2)
    tree.insert(tree.root,4)
    tree.insert(tree.root,9)
    tree.show(tree.root,0)

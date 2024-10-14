import random as rnd

class Binary_Tree:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None
    
    def __get_tree_height(self, node):
        if node is None:
            return 0
        return max(self.__get_tree_height(node.left), self.__get_tree_height(node.right))+1
    
    def get_height(self):
        if self.root is not None:
            return self.__get_tree_height(self.root)   
        
    def __add_node_rec(self, node, key):
        if node is None:
            return self.Node(key)
        elif key < node.key:
            node.left = self.__add_node_rec(node.left, key)
        else:
            node.right = self.__add_node_rec(node.right, key)
        return node
                  
    def add_node(self, key):
        self.root = self.__add_node_rec(self.root, key)
        
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key)
            self.inorder(node.right)
            
    def print_tree_as_tree(self, node, indent="", last='updown'):
        if node is not None:
            print(indent, end='')

            if last == 'updown': 
                print("Root----", end='')
                indent += "       "
            elif last == 'right':
                print("R----", end='')
                indent += "|      "
            elif last == 'left':
                print("L----", end='')
                indent += "       "

            print(node.key)

            self.print_tree_as_tree(node.right, indent, 'right')
            self.print_tree_as_tree(node.left, indent, 'left')

    def __search_key_rec(self, node, key):
        if node is None or node.key == key:
            return node
        elif key < node.key:
            return self.__search_key_rec(node.left, key)
        else:
                return self.__search_key_rec(node.right, key)
    
    def search_key(self, key):
        if self.root is not None:
            return print(f"element found: {self.__search_key_rec(self.root, key)}")
    
    def tree_minimum(self,node):
        if node.left is not None:
            return self.tree_minimum(node.left)
        else:
            return node.key
    
          
        
bt = Binary_Tree()
for i in range(7):
    bt.add_node(rnd.randint(1,100))
bt.print_tree_as_tree(bt.root)
print(f"tree height is: {bt.get_height()}")

print(f"the min element is {bt.tree_minimum(bt.root)}")
from typing import Optional

import Request


class BST:
    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key

    def __init__(self):
        self.root = None
        self.size = 0
        self.height = 0

    def find(self, time: int) -> Optional[Node]:
        current = self.root
        while current:
            if time == current.val:
                return current
            elif time < current.val:
                current = current.left
            else:
                current = current.right
        return None

    def insert(self, time: int, request: Request):
        #In case of empty tree
        if not self.root:
            self.root = self.Node(time)
            self.root.req = request
            self.root.req = request
            self.size += 1

        current = self.root
        while current:
            if time < current.val:  #If the key is in the left subtree
                #If the left of current node is None, insert
                if not current.left:   
                    current.left = self.Node(time)
                    current.left.req = request
                    self.size += 1
                    return
                current = current.left
            elif time > current.val:    #If the key is in the right subtree
                #If the right of current node is None, insert
                if not current.right:
                    current.right = self.Node(time)
                    current.right.req = request
                    self.size += 1
                    return 
                current = current.right
            else:
                current.req = request
                return

    def delete(self, time: int):
        def _delete(node: Optional[BST.Node], time: int) -> Optional[BST.Node]:
            #given node does not exist, return None
            if not node:
                return None
            
            if time < node.val:
                node.left = _delete(node.left, time)
            elif time > node.val:
                node.right = _delete(node.right, time)
            else:

                #Case 1: Node is a leaf
                if not node.left and not node.right:
                    return None
                
                #Case 2: Node has one child
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                
                #Case 3: Node has two children
                successor = self.succ(time)
                node.val = successor.val
                node.right = _delete(node.right, successor.val)

            return node
        self.root = _delete(self.root, time)


    def pred(self, time) -> Optional[Node]:
        current = self.root
        pred = None
        while current:
            if time == current.val:
                if current.left:
                    pred = current.left
                    while pred.right:
                        pred = pred.right
                    return pred
            elif time < current.val:
                current = current.left
            else:
                pred = current
                current = current.right
        return pred
                
        
    def succ(self, time) -> Optional[Node]:
        current = self.root
        succ = None
        
        while current:
            if time == current.val:
                # If right subtree exists, successor is minimum in right subtree
                if current.right:
                    succ = current.right
                    while succ.left:
                        succ = succ.left
                return succ
            elif time < current.val:
                # Keep track of the smallest value greater than time
                succ = current
                current = current.left
            else:
                current = current.right
        
        return succ

    def min(self) -> Optional[Node]:
        current = self.root
        while current.left:
            current = current.left

        return current

    def max(self) -> Optional[Node]:
        current = self.root
        while current.right:
            current = current.right

        return current

    def print(self):
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            print(current.val, end= ' ')
            current = current.right

def main():
    bst = BST()
    bst.insert(20, Request.Request("r", 10, "Airline1", "A1", "CityA", "CityB"))
    bst.insert(57, Request.Request("r", 5, "Airline2", "A2", "CityC", "CityD"))
    bst.insert(13, Request.Request("r", 15, "Airline3", "A3", "CityE", "CityF"))
    bst.insert(34, Request.Request("r", 3, "Airline4", "A4", "CityG", "CityH"))
    bst.insert(21, Request.Request("r", 7, "Airline5", "A5", "CityI", "CityJ"))
    bst.insert(22, Request.Request("r", 20, "Airline6", "A6", "CityK", "CityL"))

    if bst.root.val:
        print(bst.root.val)
    bst.print()
    
    bst.print()
    if bst.root.val:
        print(bst.root.val)
    print(bst.pred(bst.max().val).val)


if __name__ == "__main__":
    main()

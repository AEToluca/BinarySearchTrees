from typing import Optional

from Trees import Request


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
        p = self.find(time)
        if time == p.val:
            p.request = request
        elif time < p.val:
            p.left = self.Node(time, request)
        else:
            p.right = self.Node(time, request)

    def delete(self, time: int):
        
        current = self.root
        parent = None
        while current and current.val != time:
            parent = current
            if time < current.val:
                current = current.left
            else:
                current = current.right

        if not current:  
            return
        else:
            if p.left is None and p.right is None:
                p = None

        #Case 1: Node has two children
        if current.left and current.right:
            # Find predecessor and its parent
            pred = current.left
            pred_parent = current
            while pred.right:
                pred_parent = pred
                pred = pred.right
            
            # Copy predecessor's value
            current.val = pred.val
            # Delete predecessor
            if pred_parent == current:
                pred_parent.left = pred.left
            else:
                pred_parent.right = pred.left

        # Case 2: Node has at most one child
        else:
            child = current.left if current.left else current.right
            if parent is None:  # Root case
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child

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
        pass

    def max(self) -> Optional[Node]:
        pass

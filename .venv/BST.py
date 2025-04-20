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

    def find(self, time: int):
        def _find(node: Optional[BST.Node], time: int):
            if not node:
                return None
            if time == node.val:
                return node
            elif time < node.val:
                return _find(node.left, time)
            else:
                return _find(node.right, time)
        return _find(self.root, time)

    def insert(self, time: int, request: Request):
        p = self.find(time)
        if time == self.p.key:
            p.request = request
        elif time < self.p.key:
            p.left = self.Node(time, request)
        else:
            p.right = self.Node(time, request)

    def delete(self, time: int):
        pass

    def pred(self, time) -> Optional[Node]:
        pass

    def succ(self, time) -> Optional[Node]:
        pass

    def min(self) -> Optional[Node]:
        pass

    def max(self) -> Optional[Node]:
        pass

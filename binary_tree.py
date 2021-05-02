from collections import deque
from collections import namedtuple


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node

    def __str__(self):
        return str(self.val)


class Tree:

    def __str__(self):
        return self.str(self.root)

    def str(self, node: TreeNode) -> str:
        if node is None:
            return ""
        answer = ""
        if node.left is not None:
            answer += self.str(node.left)
        answer += str(node) + " "
        if node.right is not None:
            answer += self.str(node.right)
        return answer

    def __init__(self):
        self.root = None

    def __add__(self, other):
        if self.root is None:
            self.root = TreeNode(other)
            return self
        else:
            curr = self.root
            while True:
                if curr.val == other:
                    return self
                elif curr.val > other:
                    if curr.left is None:
                        curr.add_left(TreeNode(other))
                        return self
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.add_right(TreeNode(other))
                        return self
                    curr = curr.right

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        parent = None
        curr = root
        while curr is not None:
            if curr.val == key:
                if curr.left is None:
                    if parent is not None:
                        if parent.left == curr:
                            parent.left = curr.right
                        else:
                            parent.right = curr.right
                    else:
                        if curr.right is not None:
                            root.val = curr.right.val
                            root.left = curr.right.left
                            root.right = curr.right.right
                        else:
                            return None
                    return root
                elif curr.right is None:
                    if parent is not None:
                        if parent.left == curr:
                            parent.left = curr.left
                        else:
                            parent.right = curr.left
                    else:
                        if curr.left is not None:
                            root.val = curr.left.val
                            root.right = curr.left.right
                            root.left = curr.left.left
                        else:
                            return None
                    return root
                else:
                    mx = self.max(curr.left)
                    self.deleteNode(curr, mx.val)
                    mx.left = curr.left
                    mx.right = curr.right
                    if parent is not None:
                        if parent.left == curr:
                            parent.left = mx
                        else:
                            parent.right = mx
                        return root
                    else:
                        return mx

            else:
                parent = curr
                if curr.val > key:
                    curr = curr.left
                else:
                    curr = curr.right
        return root

    def max(self, node: TreeNode) -> TreeNode:
        curr = node
        while True:
            if curr.right is not None:
                curr = curr.right
            else:
                return curr


def main():
    tree = Tree()
    numbers = [int(i) for i in input().split()]
    for x in numbers:
        tree += x
    print(tree)
    print(tree.deleteNode(tree.root, int(input())))
    print(tree)


if __name__ == '__main__':
    main()

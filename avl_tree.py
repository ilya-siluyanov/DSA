from collections import deque
from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def set_right(self, right) -> None:
        if type(right) is not Node:
            return
        self.right = right
        right.parent = self

    def set_left(self, left) -> None:
        if type(left) is not Node:
            return
        self.left = left
        left.parent = self

    def __str__(self):
        return str(self.value)


class AVLTree:

    def __str__(self):
        return self.inorder_traversal(self.root)

    def inorder_traversal(self, node: Node) -> List[str]:
        answer = []
        if node.left is not None:
            answer.extend(self.inorder_traversal(node.left))
        answer.append(str(node))
        if node.right is not None:
            answer.extend(self.inorder_traversal(node.right))
        return answer

    def preorder_traversal(self, node: Node) -> List[str]:
        answer = [str(node)]
        if node.left is not None:
            answer.extend(self.inorder_traversal(node.left))
        if node.right is not None:
            answer.extend(self.inorder_traversal(node.right))
        return answer

    def postorder_traversal(self, node: Node) -> List[str]:
        answer = []
        if node.left is not None:
            answer.extend(self.inorder_traversal(node.left))
        if node.right is not None:
            answer.extend(self.inorder_traversal(node.right))
        answer.append(str(node))
        return answer

    def level_traversal(self, node: Node) -> List[str]:
        if node is None:
            return []
        q = deque()
        depth = self.height(self.root)
        answer = [[] for _ in range(depth + 2)]
        q.append((node, 1))
        while len(q) > 0:
            v, height = q.popleft()
            answer[height].append(str(v))
            if v is None:
                continue
            for child in (v.left, v.right):
                q.append((child, height + 1))

        return answer

    def __init__(self):
        self.root = None

    def __add__(self, new_node: Node) -> None:
        if self.root is None:
            self.root = new_node
            return self
        curr = self.root  # type: Node
        while True:
            if curr.value == new_node.value:
                break
            if curr.value < new_node.value:
                if curr.right is None:
                    curr.set_right(new_node)
                    break
                else:
                    curr = curr.right
            else:
                if curr.left is None:
                    curr.set_left(new_node)
                    break
                else:
                    curr = curr.left
        self.check_balancing(new_node)
        return self

    def check_balancing(self, added_leaf: Node) -> None:
        current = added_leaf
        parent = current.parent
        if parent is None:
            return
        grandparent = parent.parent
        if grandparent is None:
            return
        while grandparent not in (self.root, None):
            if abs(self.height(grandparent.left) - self.height(grandparent.right)) > 1:
                self.balance(current, parent, grandparent)
            grandparent = grandparent.parent
            parent = parent.parent
            current = current.parent

    def balance(self, current: Node, parent: Node, grandparent: Node):
        if parent == grandparent.left and current == parent.left:  # right rotation
            self.right_rotation(grandparent)
        elif parent == grandparent.left and current == parent.right:  # left-right rotation
            self.left_rotation(parent)
            self.right_rotation(grandparent)
        elif parent == grandparent.right and current == parent.left:  # right-left rotation
            self.right_rotation(parent)
            self.left_rotation(grandparent)
        elif parent == grandparent.right and current == parent.right:  # left rotation
            self.left_rotation(grandparent)

    def left_rotation(self, node: Node):
        parent = node.parent  # type: Node
        right_child = node.right  # type: Node
        if parent is not None:
            if parent.left == node:
                parent.left = right_child
            else:
                parent.right = right_child
        else:
            self.root = right_child
        right_child.parent = parent
        node.parent = right_child
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        right_child.left = node

    def right_rotation(self, node: Node):
        parent = node.parent  # type: Node
        left_child = node.left  # type: Node
        if parent is not None:
            if parent.left == node:
                parent.left = left_child
            else:
                parent.right = left_child
        else:
            self.root = left_child
        left_child.parent = parent
        node.parent = left_child
        node.left = left_child.right
        left_child.right = node
        node.left.parent = node

    def height(self, root: Node) -> int:
        if root is None:
            return 0
        q = deque()
        q.append((root, 1))
        max_depth = -1
        while len(q) > 0:
            v = q.popleft()
            v, depth = v
            max_depth = max(max_depth, depth)
            for child in (v.left, v.right):
                if child is not None:
                    q.append((child, depth + 1))
        return max_depth


def main():
    tree = AVLTree()
    for i in range(10):
        tree += Node(i)
    print(tree.inorder_traversal(tree.root))
    print(tree.preorder_traversal(tree.root))
    print(tree.postorder_traversal(tree.root))
    print(tree.level_traversal(tree.root))


if __name__ == '__main__':
    main()

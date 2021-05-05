from enum import Enum
from collections import deque
from typing import List
class Color(Enum):
  BLACK = "BLACK",
  RED = "RED"


class Node:
  
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None
    self.parent = None
    self.color = Color.RED

  def __str__(self):
    return str(self.value)
  
  def set_right(self, node):
    self.right = node
    node.parent = self
  
  def set_left(self, node):
    self.left = node
    node.parent = self


class RedBlackTree:
 
  def __init__(self):
    self.null_node = Node(None)
    self.null_node.color = Color.BLACK
    self.root = self.null_node

  def __str__(self):
    return str(self.level_traversal(self.root))
  
  def generate_node(self, value) -> Node:
    new_node = Node(value)
    new_node.left = self.null_node
    new_node.right = self.null_node
    new_node.parent = self.null_node
    return new_node

  def insert(self, value):
      new_node = self.generate_node(value)
      if self.root is self.null_node:
        self.root = new_node
      else:
        curr = self.root
        while curr is not self.null_node:
          if curr.value == new_node.value:
            return
          elif curr.value < new_node.value:
            if curr.right is self.null_node:
              curr.set_right(new_node)
              break
            else:
              curr = curr.right
          else:
            if curr.left is self.null_node:
              curr.set_left(new_node)
              break
            else:
              curr = curr.left
      self.insert_fixup(new_node)


  def insert_fixup(self, new_node):
    while new_node.parent.color == Color.RED:
      #case 1: uncle is red too
      #case 2: uncle is black, new_node is right child
      #case 3: similar to c.2, but new_node is left child
      grandparent = new_node.parent.parent
      if grandparent.left is new_node.parent: #new_node is a left child
        uncle = grandparent.right
        if uncle.color == Color.RED:  #case 1
          uncle.color = Color.BLACK
          new_node.parent.color = Color.BLACK
          grandparent.color = Color.RED
          new_node = grandparent
        else:
          if new_node.parent.right is new_node:  #case 2
            self.left_rotation(new_node.parent) #new_node is in new_node.parent place 
          new_node.color = Color.BLACK
          new_node.parent.color = Color.RED
          self.right_rotation(new_node.parent)
      else: #new_node is a right child
        uncle = grandparent.left
        if uncle.color == Color.RED:  #case 1
          uncle.color = Color.BLACK
          new_node.parent.color = Color.BLACK
          grandparent.color = Color.RED
          new_node = grandparent
        else:
          if new_node.parent.left is new_node: #case 2
            self.right_rotation(new_node.parent)
          else:
            new_node = new_node.parent 
          new_node.color = Color.BLACK #case 3
          new_node.parent.color = Color.RED
          self.left_rotation(new_node.parent)
    self.root.color = Color.BLACK
  #1. Left substree of the right child becomes right subtree of the node
  #2. a parent of the node becomes the parent of the right child
  #3. right child becomes a parent for a node
  def left_rotation(self, node):
    right_child = node.right
    node.right = right_child.left
    if right_child.left is not self.null_node:
      right_child.left.parent = node
    right_child.parent = node.parent
    if node.parent is self.null_node:
      self.root = right_child
    else:
      if node is node.parent.left:
        node.parent.left = right_child
      else:
        node.parent.right = right_child
    right_child.left = node
    node.parent = right_child

  def right_rotation(self, node):
    left_child = node.left
    node.left = left_child.right
    if left_child.right is not self.null_node:
      left_child.right.parent = node
    left_child.parent = node.parent
    if node.parent is self.null_node:
      self.root = left_child
    else:
      if node.parent.left is node:
        node.parent.left = left_child
      else:
        node.parent.right = left_child
    left_child.right = node
    node.parent = left_child

  def level_traversal(self, node: Node) -> List[str]:
        if node is None:
            return []
        q = deque()
        depth = self.height(self.root)
        answer = [[] for _ in range(depth + 2)]
        q.append((node, 1))
        while len(q) > 0:
            v, height = q.popleft()
            answer[height].append(str(v)+" "+(str(v.color.name) if v is not None else "" ))
            if v is self.null_node:
                continue
            for child in (v.left, v.right):
                q.append((child, height + 1))
        del answer[0]
        return answer

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
  tree = RedBlackTree()
  for i in range(1, 10):
    tree.insert(i)

  print(str(tree))


if __name__ == '__main__':
  main()
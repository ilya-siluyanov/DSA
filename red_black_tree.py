class Color(Enum):
  BLACK = "BLACK",
  RED = "RED"


class Node:
  
  def __init__(self, value = None, color=Color.BLACK, left=None, right=None):
    self.value = value
    self.left = None
    self.right = None
    self.parent = None
    self.color = color


class RedBlackTree:
 
  def __init__(self):
    self.nullNode = Node()
    self.root = self.nullNode
  
  def insert(self, value):
    newNode = Node(value, Color.RED)
    if self.root is self.nullNode:
      newNode.parent = self.nullNode
      self.root = newNode
    else:
      curr = self.root
      while curr is not None:
        if curr.value == newNode.value:
          return
        elif curr.value < newNode.value:
          if curr.right is None:
            curr.right = newNode
          else:
            curr = curr.right
        else:
          if curr.left is None:
            curr.left = newNode
          else:
            curr = curr.left
    self.insert_fixup(newNode)
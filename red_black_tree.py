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
  
  def generate_node(self, value) -> Node:
    new_node = Node(value)
    new_node.left = self.null_node
    new_node.right = self.null_node
    new_node.parent = self.null_node

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
          if curr.right is None:
            curr.set_right(new_node)
          else:
            curr = curr.right
        else:
          if curr.left is None:
            curr.set_left(new_node)
          else:
            curr = curr.left
    self.insert_fixup(new_node)

    def insert_fixup(self, new_node):
      while new_node.parent.color == Color.RED:
        #case 1: uncle is red too
        #case 2: uncle is black, new_node is right child
        #case 3: similar to c.2, but new_node is left child
        if new_node.parent.parent.left is new_node.parent: #new_node is a left child
          uncle = new_node.parent.parent.right
          if uncle.color == Color.RED:  #case 1
            uncle.color = Color.BLACK
            new_node.parent.color = Color.BLACK
            new_node.parent.parent.color = Color.RED
            new_node = new_node.parent.parent
          else:
            if new_node.parent.right is new_node:  #case 2
              new_node = new_node.parent
              self.left_rotation(new_node)
            new_node.color = Color.BLACK
            new_node.parent = Color.RED
            new_node = new_node.parent
            self.right_rotation(new_node)
        else: #new_node is a right child
          pass
    def left_rotation(self, node):
      pass
    def right_rotation(self, node):
      pass


        
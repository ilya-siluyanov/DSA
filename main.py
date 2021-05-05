from red_black_tree import *
def main():
  tree = RedBlackTree()
  for i in range(1, 10):
    tree.insert(i)
  
  print(str(tree))


if __name__ == '__main__':
  main()
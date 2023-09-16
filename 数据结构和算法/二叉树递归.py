class TreeNode:
  def __init__(self,val,left=None,right=None):
    self.value = val
    self.leftChild = left
    self.rightChild = right

  def search(self, value, node):
    """搜索"""
    if node is None or node.value == value:
      return node
    elif value < node.value:
      return self.search(value, node.leftChild)
    else:
      return self.search(value, node.rightChild)
  
  def insert(self,value, node):
    """插入"""
    if value < node.value:
      if node.leftChild is None:
        node.leftChild = TreeNode(value)
      else:
        self.insert(value, node.leftChild)
    elif value > node.value:
      if node.rightChild is None:
        node.rightCHild = TreeNode(value)
      else:
        self.insert(value, node.rightChild)


  def traverse_and_print(self, node):
    """中序遍历"""
    if node is None:
      return
    self.traverse_and_print(node.leftChild)
    print(node.value)
    self.traverse_and_print(node.rightChild)


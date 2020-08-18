class Node
  attr_accessor :val, :left, :right
  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

def insert(root, node)
  if root.nil?
    root = node
  end
  if root.val > node.val
    if root.left.nil?
      root.left = node
    elsif
      insert(root.left, node)
    end
  else
    if root.right.nil?
      root.right = node
    else
      insert(root.right, node)
    end
  end
end


def search(root, key)
  return root if root.nil? or root.val == key
  return search(root.right, key) if root.val < key
  return search(root.left, key)
end


def min(root)
  curr = root
  until curr.left.nil?
    curr = curr.left
  end
  curr
end

def delete(root, key)
  # If we don't find key
  return root if root.nil?

  # If the root's val is less than key we are searching for
  if root.val < key
    root.right = delete(root.right, key)
  elsif root.val > key
    # If the root's val is bigger than key we are searching for
    root.left = delete(root.left, key)
  else
    # If it is the match
    # Works for leaf nodes as well as with nodes with 1 child
    if root.left.nil?
      tmp = root.right
      root = nil
      return tmp
    elsif root.right.nil?
      tmp = root.left
      root = nil
      return tmp
    end

    # If it has multiple child
    # Copy Either the minimum from right sub-tree or maximum from left sub-tree
    tmp = min(root.right)

    # replace the current node with the minimum node on the right sub -tree
    root.val = tmp.val

    # delete the minimum node from the right subtree
    root.right = delete(root.right, tmp.val)
  end
  root
end

def inorder(root)
  if root
    inorder(root.left)
    print root.val, ' '
    inorder(root.right)
  end
end

r = Node.new(50)
insert(r, Node.new(20))
insert(r, Node.new(40))
insert(r, Node.new(70))
insert(r, Node.new(60))
insert(r, Node.new(80))
inorder(r)

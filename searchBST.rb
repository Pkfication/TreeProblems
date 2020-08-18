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

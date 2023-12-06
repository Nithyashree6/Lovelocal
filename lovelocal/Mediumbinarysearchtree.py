class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    # If both nodes are greater than the root, search in the right subtree
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    # If both nodes are smaller than the root, search in the left subtree
    elif p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    # Otherwise, the current root is the LCA
    else:
        return root

# Test cases
# Creating the tree
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

# Test cases
p = root.left  
q = root.right  
result = lowestCommonAncestor(root, p, q)
print(result.val) 

p = root.left  
q = root.left.right  
result = lowestCommonAncestor(root, p, q)
print(result.val)  

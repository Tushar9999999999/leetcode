# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True 
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))
    
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s1 = [[root, subRoot]]
        while s1:
            x, y = s1.pop()
            if not x and not y:
                continue
            if not x or not y or x.val != y.val:
                return False
            s1.append([x.left, y.left])
            s1.append([x.right, y.right])
        return True


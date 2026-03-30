# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            a = stack.pop()
            if not a or not subRoot:
                continue
            if a.val == subRoot.val:
                s1 = [[a, subRoot]]
                while s1:
                    x, y = s1.pop()
                    if not x and not y:
                        continue
                    if not x or not y or x.val != y.val:
                        return False
                    s1.append([x.left, y.left])
                    s1.append([x.right, y.right])
                return True
            stack.append(a.left)
            stack.append(a.right)
        return False
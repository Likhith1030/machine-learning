# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        def likky(node):

            if not node:
                return None
            
            l = likky(node.left)

            if l is not None:
                return l
            
            self.k -= 1

            if self.k == 0: return node.val

            return likky(node.right)

    
        return likky(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def likky(node):

            if not node:
                return None
            
            l = likky(node.left)
            r = likky(node.right)

            node.left = r
            node.right = l

            return node

        likky(root)

        return root
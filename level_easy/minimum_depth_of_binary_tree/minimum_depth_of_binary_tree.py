# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def countBalance(minDepth):
            if minDepth is None :
                return 0

            leftHeight = countBalance(minDepth.left)
            rightHeight = countBalance(minDepth.right)
            if leftHeight == 0 :
                return 1 + rightHeight
            if rightHeight == 0 :
                return 1 + leftHeight

            return 1 + min(rightHeight, leftHeight)

        return countBalance(root)

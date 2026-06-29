# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def countBalance(maxDepth) :
            if maxDepth is None :
                return 0

            leftHeight = countBalance(maxDepth.left)
            rightHeight = countBalance(maxDepth.right)

            if leftHeight is False or rightHeight is False :
                return False

            if abs(leftHeight - rightHeight) > 1 :
                return False

            return 1 + max(leftHeight, rightHeight)

        return countBalance(root) is not False

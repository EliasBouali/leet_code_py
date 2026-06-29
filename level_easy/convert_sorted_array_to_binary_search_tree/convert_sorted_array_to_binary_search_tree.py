class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def sortedArray(array):
            if not array:
                return None
            mid = len(array) // 2
            node = TreeNode(array[mid])
            node.left = sortedArray(array[:mid])
            node.right = sortedArray(array[mid + 1:])
            return node
        return sortedArray(nums)

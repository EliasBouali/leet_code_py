class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i , val_i in enumerate(nums):
            for j , val_j  in enumerate(nums [i+ 1:], start=i + 1):
                if (val_i + val_j) == target:
                    return [i, j]

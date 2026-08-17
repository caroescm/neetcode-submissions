class Solution:
    def findMin(self, nums: List[int]) -> int:
        num = sorted(nums)
        return num[0]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_nums = {}

        for i, num in enumerate(nums):
            look = target - num
            if look not in my_nums:
                my_nums[num] = i
            else:
                idx = [i, my_nums[look]]
                return sorted(idx)
                
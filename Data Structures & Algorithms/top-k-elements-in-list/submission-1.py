from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_nums = Counter(nums)

        return heapq.nlargest(k, my_nums, key = my_nums.get)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        parsed = sorted(set(nums))
        answ = {parsed[0]}
        largest_len = 1

        for prev, sec in zip(parsed, parsed[1:]):
            if sec - prev != 1:
                answ.clear()
            answ.add(sec)
            largest_len = max(largest_len, len(answ))

        return largest_len
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        window = []

        longest = 0

        for ch in s:
            while ch in seen:
                removed = window.pop(0)
                seen.remove(removed)
            seen.add(ch)
            window.append(ch)
            longest = max (longest, len(window))

        return longest
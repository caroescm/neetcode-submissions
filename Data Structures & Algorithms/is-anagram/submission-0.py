class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        for ch in s:
            if ch in s_count:
                s_count[ch] += 1
            else:
                s_count[ch] = 1
        
        t_count = {}
        for ch in t:
            if ch in t_count:
                t_count[ch] +=1
            else:
                t_count[ch] = 1
        
        return s_count == t_count 
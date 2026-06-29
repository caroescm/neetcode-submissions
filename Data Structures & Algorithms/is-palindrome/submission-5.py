class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        b = s[::-1]
        if b == s:
            return True
        else:
            return False
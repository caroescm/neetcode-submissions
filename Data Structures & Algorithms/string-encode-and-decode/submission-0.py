class Solution:

    def encode(self, strs: List[str]) -> str:
        answ = ""
        for s in strs:
            answ +=  str(len(s)) + "#" + s
        return answ

    def decode(self, s: str) -> List[str]:
            result = []
            i = 0

            while i < len(s):
                j = i
                while s[j] != "#":
                    j += 1
                n = int(s[i:j])
                result.append(s[j+1 : j+1+n])
                i = j + 1 + n

            return result
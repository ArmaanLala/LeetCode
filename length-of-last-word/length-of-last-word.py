class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if (s == ""):
            return 0
        words = s.split(" ")
        return (len(words[-1]))
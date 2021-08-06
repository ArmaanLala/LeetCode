class Solution:
    def replaceDigits(self, s: str) -> str:
        return_string = ""
        if (len(s) == 0):
            return return_string
        for i in range (0,len(s),2):
            return_string += s[i]
            if (i + 1 < len(s)):
                return_string += chr(ord(s[i]) + int(s[i+1]))
        return return_string
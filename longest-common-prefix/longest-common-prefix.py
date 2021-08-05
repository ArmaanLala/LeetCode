class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        flag = False
        for i in range(len(strs[0]) + 1):
            for word in strs:
                # print(strs[0][0:i])
                if (strs[0][0:i] != word[0:i]):
                    flag = True
                    break
                
            if (flag):
                return prefix
            else:
                prefix = strs[0][0:i]
        return prefix
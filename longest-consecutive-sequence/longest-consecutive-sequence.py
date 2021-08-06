class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        
        longest = 0
        current = 1
        
        for i in hashSet:
            if (i -1) not in hashSet:
                current = 1
                val = i
                while ((val + 1) in hashSet):
                    current +=1
                    val += 1
                if (current > longest):
                    longest = current
        return longest if len(nums) > 0 else 0
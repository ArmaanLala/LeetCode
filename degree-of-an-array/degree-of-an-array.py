import statistics
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        vals = statistics.multimode(nums)
        lengths = [(len(nums) - 1 - nums[::-1].index(val)) - nums.index(val) for val in vals]
        return min(lengths) + 1
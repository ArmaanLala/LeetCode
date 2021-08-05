class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        maxV = dp[0]
        for i in range(1,len(nums)):
            dp.append(max(nums[i],dp[i-1] + nums[i]))
            if (dp[-1] > maxV):
                maxV = dp[-1]
        return maxV
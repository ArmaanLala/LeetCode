class Solution:
    def rob(self, nums: List[int]) -> int:
        dp= [0,0]
    
        for i in range(0,len(nums)):
            dp.append(max(dp[-1], dp[-2] + nums[i]))
        return(max(dp))
class Solution:
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        index = len(nums) - 1
        currentValue = 0
        self.dict = {}
        return self.dynamicRecur(nums, target, index, currentValue)
        
    def dynamicRecur(self, nums, target, index, currentValue):
        
        if (index, currentValue) in self.dict:
            return self.dict[(index, currentValue)]
        
        if index < 0 and currentValue == target:
            return 1
        if index < 0:
            return 0 
        
        postiveWays = self.dynamicRecur(nums, target, index-1, currentValue + nums[index])
        negativeWays = self.dynamicRecur(nums, target, index-1, currentValue + -nums[index])
        
        self.dict[(index, currentValue)] = postiveWays + negativeWays
        return self.dict[(index, currentValue)]
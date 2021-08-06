class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        
        ret = [1 for i in nums]
        
        for i in range(len(nums)):
            ret[i] *= left
            ret[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]
            
        return ret
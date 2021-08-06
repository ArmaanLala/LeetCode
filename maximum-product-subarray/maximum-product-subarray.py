class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # have variables for biggest negative and biggest positive
        # The reason is because if we multiply two negatives together, 
        # we get a positive which could be the max
        minVal = nums[0]
        maxVal = nums[0]
        ans = maxVal
        
        for i in range(1,len(nums)):
            # temp is for use after maxVal has been calculated
            temp = (min(nums[i],minVal*nums[i],maxVal*nums[i]))
            maxVal =(max(nums[i],maxVal*nums[i],minVal*nums[i]))
            minVal = temp
            
            ans = max(ans,maxVal)
            
        return (ans)
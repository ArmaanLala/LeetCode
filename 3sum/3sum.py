class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        retList = set()
        
        i = 0
        
        for i in range (len(nums)-2):
            
            j = i + 1
            k = len(nums) - 1
            
            while(j < k):
                total = nums[i] + nums[j] + nums[k]
                if (total == 0):
                    retList.add((nums[i],nums[j],nums[k]))
                    
                if (total < 0):
                    j +=1
                else:
                    k -= 1
        
        return(retList)
        
        
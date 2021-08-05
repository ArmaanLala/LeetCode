class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        
        left,right = 0 , len(height) - 1
        maxArea = min(height[left],height[right]) * (right-left)
        
        while(left < right):
            area = min(height[left],height[right]) * (right-left)
            if (height[left] < height[right]):
                left +=1
            else:
                right -=1
            
            if(area > maxArea):
                maxArea = area
        
        return maxArea
                
            
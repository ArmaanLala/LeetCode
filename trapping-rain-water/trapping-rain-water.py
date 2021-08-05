class Solution:
    def trap(self, height: List[int]) -> int:
        if (len(height) < 3):
            return 0
        leftMax = [height[0]]
        rightMax= [height[-1]]
        
        for i in range(1, len(height)):
            leftMax.append(max(leftMax[-1],height[i-1]))
        for i in range(len(height) - 1, 0,-1):
            rightMax.append(max(rightMax[-1],height[i]))
        rightMax = rightMax[::-1]
            
        print(leftMax)
        print(rightMax)
        total = 0
        
        
        
        for i in range(1,len(height)-1):
            val = (min(leftMax[i],rightMax[i]) - height[i])
            total += val if val > 0 else 0
            print(val)
        return total
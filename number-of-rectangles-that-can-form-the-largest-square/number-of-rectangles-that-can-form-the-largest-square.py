class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        dict= {}
        
        maxVal = 0
        
        for rect in rectangles:
            val = min(rect)
            
            if val not in dict:
                dict[val] = 1
                
            else:
                dict[val] +=1 
                
            maxVal = max(maxVal,val)
        return dict[maxVal]
            
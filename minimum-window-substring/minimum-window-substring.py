class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        requiredVals = Counter(t)
        uniqueChar = len(requiredVals)
        
        anchor = 0
        endPoint = 0
        
        currentWindowCounts = {}
        
        conditionsMet = 0
        
        answer = (float('inf'),None,None)
        
        while(endPoint < len(s)):
            
            currentChar = s[endPoint]
            currentWindowCounts[currentChar] = currentWindowCounts.get(currentChar,0) + 1
            
            if (currentChar in requiredVals and currentWindowCounts[currentChar] == requiredVals[currentChar]):
                conditionsMet += 1
                
            while ( anchor <= endPoint and conditionsMet == uniqueChar):
                char = s[anchor]
            
                if ((endPoint-anchor) + 1) < answer[0]:
                    answer = (endPoint - anchor + 1, anchor, endPoint)
                
                currentWindowCounts[char] -=1
                
                if (char in requiredVals and currentWindowCounts[char] < requiredVals[char]):
                    conditionsMet -=1
                
                anchor +=1
        
            endPoint +=1
        
        return "" if (answer[0] == float('inf')) else s[answer[1]:answer[2] + 1]
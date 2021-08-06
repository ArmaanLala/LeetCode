class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        timing = []
        for i in range (0, len(releaseTimes) - 1):
            timing.append(releaseTimes[i+1] - releaseTimes[i])
        
        timing.insert(0,releaseTimes[0])
        print(timing)
        keys = []
        maxVal = max(timing)
        for i in range (len(timing)):
            if (timing[i]== maxVal):
                keys.append(keysPressed[i])
        return max(keys)
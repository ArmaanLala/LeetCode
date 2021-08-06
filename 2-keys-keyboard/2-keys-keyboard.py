class Solution:
    def minSteps(self, n: int) -> int:
        if (n == 1):
            return 0
        if (n%2 == 1):
            for i in range(n-1,2,-1):
                if(n%i == 0):
                    return int(n/i + self.minSteps(i))
            return n
        else:
            return int(2 + self.minSteps(int(n/2)))
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+2)]
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        if (n < 4):
            return dp[n]
        
        for i in range(3,n+2):
            x = [t*dp[i-t] for t in range(2,i)]
            # print(x)
            # print(max(x))
            dp[i] = max(x)
            
        return(dp[n+1])
        
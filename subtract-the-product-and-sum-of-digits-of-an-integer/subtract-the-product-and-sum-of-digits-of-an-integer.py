class Solution:
    def subtractProductAndSum(self, n: int) -> int:
    
        return self.mult(n) - self.sum(n)
    
    def sum(self, n: int) -> int:
        ans = 0
        while (n != 0):
            ans += n%10
            n = int(n/10)
        print(ans)
        return ans
    
    def mult(self, n: int) -> int:
        ans = 1
        while (n != 0):
            ans *= n%10
            n = int(n/10)
        print(ans)
        return ans
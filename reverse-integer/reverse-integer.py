class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        neg = x < 0
        if (neg):
            x *=-1
        while (x != 0 ):
            print(ans)
            ans *= 10
            ans += x%10
            x /= 10
            x = int(x)
        if (neg):
            ans *= -1
        if (ans > (2**31 -1) or ans < -1*(2**31)):
            return 0
        return ans
            
        
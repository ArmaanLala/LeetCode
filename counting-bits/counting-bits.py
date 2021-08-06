class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]
        for i in range(1,n+1):
            arr.append(arr[i//2] + (i&1))
            
        return arr
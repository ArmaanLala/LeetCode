class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dyn = arr.copy()
        for i in range (len(arr)):
            for j in range (k):
                if (i >= j):
                    dyn[i] = max(dyn[i], (max(arr[i-j:i+1])*(j+1))+(dyn[i-j-1] if (i-j) > 0 else 0))
        return dyn[-1]
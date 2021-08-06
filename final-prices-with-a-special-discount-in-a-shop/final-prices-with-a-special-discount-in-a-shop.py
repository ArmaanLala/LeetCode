class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        final = []
        for i in range(len(prices)):
            for j in range(i + 1,len(prices)):
                if (prices[i] >= prices[j]):
                    final.append(prices[i] - prices[j])
                    break
            if (len(final) <= i):
                final.append(prices[i])
        return final
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ws = 0
        prof = 0

        for we in range(1, len(prices)):
            if prices[we] <= prices[ws]:
                ws = we
            else:
                prof = max(prof, prices[we] - prices[ws])
        
        return prof
            
        
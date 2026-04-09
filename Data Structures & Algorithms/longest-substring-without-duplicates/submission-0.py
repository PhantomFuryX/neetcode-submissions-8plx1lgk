class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ws = 0
        res = set()
        maxres = 0
        for we in range(len(s)):
            while s[we] in res:
                res.remove(s[ws])
                ws += 1
            
            res.add(s[we])
            
            maxres = max(maxres, we - ws + 1)
        
        return maxres
        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        wins = 0
        maxval = 0
        currval = 0
        
        freq = {}
        maxfreq = 0
        for wine in range(len(s)):
            freq[s[wine]] = freq.get(s[wine], 0) + 1
            maxfreq = max(maxfreq, freq[s[wine]])

            while ((wine -wins + 1) - maxfreq > k):
                freq[s[wins]] -= 1
                wins += 1
            
            maxval = max(maxval, wine - wins + 1)
        
        return maxval

        
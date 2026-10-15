class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ws = 0
        mlen = 1
        wins = set()
        if(len(s) == 0):
            return 0
        for we in range(len(s)):
            while s[we] in wins:
                wins.discard(s[ws])
                ws += 1
            wins.add(s[we])
            mlen = max(mlen, we - ws + 1)

        return mlen
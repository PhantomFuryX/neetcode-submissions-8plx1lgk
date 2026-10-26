class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ws = we = 0
        res = 0
        wc = {}
        for we in range(len(s)):
            wc[s[we]] = wc.get(s[we], 0) + 1
            #print(len(wc), (we - ws + 1))
            while((we - ws + 1) - max(wc.values()) > k ):
                wc[s[ws]] -= 1
                ws += 1
            res = max(res, we - ws + 1)

        return res
        
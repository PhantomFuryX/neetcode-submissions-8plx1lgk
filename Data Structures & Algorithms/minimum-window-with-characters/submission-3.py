class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ws = 0
        res =""
        countT, window = {}, {}
        ts = len(t)
        if len(s) < ts or ts == 0:
            return res


        for i in t:
            countT[i] = countT.get(i, 0) + 1
        #print(need)

        have, need = 0, len(countT)
        resin, reslen = [-1, -1], float("infinity")
        for we in range(len(s)):
            c = s[we]  
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if((we - ws + 1) < reslen):
                    resin = [ws, we]
                    reslen = (we - ws + 1)
                window[s[ws]] -= 1
                if s[ws] in countT and window[s[ws]] < countT[s[ws]]:
                    have -= 1
                ws += 1
        ws, we = resin
        return s[ws: we + 1] if reslen != float("infinity") else ""
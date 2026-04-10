class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        window = len(s1)
        s1 = "".join(sorted(s1))

        for i in range(0, len(s2)):
            print("".join(sorted(s2[i:i + window])))
            if s1 in "".join(sorted(s2[i:i + window])):
                return True
            else:
                continue
        
        return False
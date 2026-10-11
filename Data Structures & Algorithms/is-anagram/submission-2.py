class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        um = {}
        um1 = {}
        for i in s:
            um[i] = um.get(i, 0) + 1
        for j in t:
            um1[j] = um1.get(j, 0) + 1
        return um == um1
        
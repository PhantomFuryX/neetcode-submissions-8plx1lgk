from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sm = {}
        for i in strs:
            if ("".join(sorted(i))) not in sm:
                sm["".join(sorted(i))] = []
            sm["".join(sorted(i))].append(i)                
        # print(sm)
        return list(sm.values())

        

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}
        for i in strs:
            sortedstr = "".join(sorted(i))
            if sortedstr not in anag:
                anag[sortedstr] = [i]
            else:
                anag[sortedstr].append(i)

        return list(anag.values())
            

        
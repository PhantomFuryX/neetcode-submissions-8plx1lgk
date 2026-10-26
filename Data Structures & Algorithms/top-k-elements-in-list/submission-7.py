from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums).most_common(k)
        fin = []
        for i in res:
            fin.append(i[0])
        return fin
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        setn = {}
        res = []
        for i in nums:
            setn[i] = setn.get(i, 0) + 1
        setn = sorted(setn.items(), key = lambda item: item[1], reverse=True)
        for i in setn:
            res.append(i[0])
        return res[:k]
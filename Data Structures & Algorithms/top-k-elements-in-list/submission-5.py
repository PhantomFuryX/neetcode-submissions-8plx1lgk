class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        ans = []
        for i in nums:
            if i in freqmap:
                freqmap[i] += 1
            else:
                freqmap[i] = 1
        
        count = 0
        #print(freqmap)
        freqmap = dict(sorted(freqmap.items(), key=lambda item: item[1], reverse=True))
        #print(freqmap)
        for i in freqmap:
            if count < k:
                ans.append(i);
                count +=1

        return ans
        
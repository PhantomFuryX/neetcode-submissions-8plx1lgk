class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxone = 0
        currone = 0
        for i in nums:
            if i == 1:
                currone += 1
                maxone = max(maxone, currone)
            else:
                currone = 0
            #print(maxone)
        #print(maxonearr)
            
        
        return maxone
            
        
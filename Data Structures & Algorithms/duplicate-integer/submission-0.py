class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = {}
        for i in nums:
            if i in unique:
                return True
            else:
                unique[i] = 1
        
        return False
        
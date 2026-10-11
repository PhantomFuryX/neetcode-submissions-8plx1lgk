class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = []
        for i in nums:
            if i not in unique:
                unique.append(i)
                #print(unique)
            else:
                return True
        return False
            

        
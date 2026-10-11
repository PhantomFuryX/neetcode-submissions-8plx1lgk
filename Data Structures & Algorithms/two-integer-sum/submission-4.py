class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        for i,val in enumerate(nums):
            if target - val in prevmap:
                return [prevmap[target - val], i]
            prevmap[val] = i
                


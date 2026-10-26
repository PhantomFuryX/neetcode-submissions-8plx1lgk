from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = Counter(nums)
        if len(nums) == 0:
           return False
        print(set_nums[1])
        for key, value in set_nums.items():
            if (value > 1):
                return True
        return False
        
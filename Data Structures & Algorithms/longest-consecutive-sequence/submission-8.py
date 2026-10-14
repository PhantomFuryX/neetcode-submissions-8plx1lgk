class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_so_far = 0
        nums_set = set(nums)
        if len(nums) == 1:
            return 1
        for i in nums_set:
            if i-1 not in nums_set:
                curr_max = 1
                while (i + curr_max) in nums_set:
                    curr_max += 1
                max_so_far = max(max_so_far, curr_max)
        
        return max_so_far
            
        
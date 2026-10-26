class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        for i in nums:
            if i - 1 not in nums:
                leng = 1
                while (i + leng) in nums:
                    leng += 1
                max_len = max(max_len, leng)
        return max_len     
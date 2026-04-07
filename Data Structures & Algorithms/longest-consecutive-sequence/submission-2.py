class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        max_seq = 0
        print(values)
        for n in values:
            if n - 1 not in values:
                start = n
                seq_len = 0

                while start in values:
                    seq_len += 1
                    start += 1

                max_seq = max(max_seq, seq_len)
        
        return max_seq

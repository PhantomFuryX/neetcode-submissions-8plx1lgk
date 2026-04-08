class Solution:
    def threeSum(self, nums2: List[int]) -> List[List[int]]:
        nums2 = sorted(nums2)
        res = []
        print(nums2)
        i = 0
        while nums2[i] <= 0 and i <  len(nums2) - 2:
            if i > 0 and nums2[i] == nums2[i - 1]:
                i += 1
                continue

            possiblenums = self.getthreenums(nums2[i + 1:], -nums2[i])
            res += possiblenums
            i+= 1

        return res

    def getthreenums(self, numbers: List[int], tar: int):
        l , r = 0, len(numbers) - 1
        out = []
        while l < r :
            if l > 0 and numbers[l] == numbers[l - 1]:
                l += 1
                continue
            s = numbers[l] + numbers[r]
            if s < tar:
                l += 1
            elif s > tar:
                r -= 1
            else:
                out.append([-tar, numbers[l], numbers[r]])
                l += 1
                r -= 1
        
        return out
            

        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        currarea = 0
        maxarea = 0
        while(l < r):
            if(heights[l] > heights[r] and heights[r] != 0):
                currarea = (r - l) * heights[r]
                r -= 1
            elif(heights[l] <= heights[r] and heights[l] != 0):
                currarea = (r - l) * heights[l]
                l += 1
            else:
                currarea = 0
                l += 1
                r -= 1
            maxarea = max(maxarea, currarea)
        
        return maxarea


        
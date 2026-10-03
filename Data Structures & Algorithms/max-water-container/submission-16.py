class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l,r = 0, len(heights)-1

        while l < r:
            h = min(heights[l],heights[r])
            w = r - l 
            best = max(best,h*w)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best
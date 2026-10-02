class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        best = 0

        for x in nums:
            if x-1 not in seen:
                y = x
                while y in seen:
                    y += 1
                best = max(best,y-x)
        return best
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seen:
                return [seen[compliment],i]
            seen[nums[i]] = i
        return []

        class solution:
            def twoSum(self,nums,target):
                for i in range(len(nums)):
                    for j in range(i+1,len(nums)):
                        if nums[i] + nums[j] == target:
                            return [i,j]
                return []
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        freq = {0:1}
        for x in nums:
            prefix += x
            need = prefix - k
            if need in freq:
                count += freq[need]
            
            freq[prefix] = freq.get(prefix,0) + 1
        return count
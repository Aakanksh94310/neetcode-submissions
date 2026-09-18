class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord("a")] += 1
        for ch in t:
            if freq[ord(ch) - ord("a")] == 0:
                return False
            freq[ord(ch)-ord("a")] -= 1
        return True
        
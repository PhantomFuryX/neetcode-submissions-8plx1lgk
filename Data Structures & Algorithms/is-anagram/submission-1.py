class Solution:
    def get_freq(self, s: str):
        element_counts = {}

        for item in s:
            if item in element_counts:
                element_counts[item] += 1
            else:
                element_counts[item] = 1
        
        return element_counts
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if self.get_freq(s) == self.get_freq(t):
            return True
        return False

        
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in s:
            d1[i] += 1
        for i in t:
            d2[i] += 1
        if d1==d2:
            return True
        else:
            return False
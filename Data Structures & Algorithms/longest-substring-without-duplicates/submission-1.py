class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a, b = 0, 0
        maxs, res = 0, 0
        while b < len(s):
            if s[b] in s[a:b]: 
                maxs = 0
                a+=1
                b=a
            else:
                maxs+=1
                b+=1
            res = max(res, maxs)
        return res
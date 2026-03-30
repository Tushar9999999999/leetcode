class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        itr = set(nums)
        maxr = 0
        for i in itr:
            temp = i
            res = 0
            while temp in itr:
                res += 1
                temp += 1
            maxr = max(res, maxr)
        return maxr
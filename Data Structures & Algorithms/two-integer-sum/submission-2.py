class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        n = sorted(nums)
        for i in range(len(nums)):
            d[nums[i]] = i

        i, j = 0, len(n)-1
        while j>i:
            s = n[i] + n[j]
            if s == target:
                return [d[n[i]],d[n[j]]]
            if s > target:
                j-=1
            else:
                i+=1
        return []

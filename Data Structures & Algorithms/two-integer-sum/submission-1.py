class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = sorted(nums)
        i, j = 0, len(n)-1
        while j>i:
            s = n[i] + n[j]
            if s == target:
                return [i,j]
            if s > target:
                j-=1
            else:
                i+=1
        return []

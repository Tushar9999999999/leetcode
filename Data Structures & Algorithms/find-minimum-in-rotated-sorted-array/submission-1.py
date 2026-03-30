class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        low = nums[0]
        while l<=r:
            mid = (l+r)//2
            # low = min(low, nums[mid])
            if nums[l] < nums[r]:
                low = min(low, nums[l])
                break
            low = min(low, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid+1
            else:
                r = mid-1
        return low

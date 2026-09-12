class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]
        else:
            minVal = nums[r]

            while l <= r:
                mid = (l + r) // 2
                
                if nums[mid] > minVal:
                    l = mid + 1
                else:
                    r = mid - 1
                
                minVal = min(minVal, nums[mid])

            return minVal



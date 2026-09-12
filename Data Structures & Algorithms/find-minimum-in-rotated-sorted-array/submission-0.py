class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # while l <= r:
        #     mid = (l + r) // 2

        #     if 

        if nums[l] < nums[r]:
            return nums[l]
        else:
            val = nums[r]

            while r >= 0 and nums[r - 1] < val:
                r -= 1
            
            return nums[r]

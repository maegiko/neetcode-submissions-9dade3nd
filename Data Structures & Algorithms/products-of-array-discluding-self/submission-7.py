class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_pre = []
        right_pre = [1] * len(nums)

        running = 1
        for num in nums:
            left_pre.append(running)
            running *= num
        
        running = 1
        for i in range(len(nums) - 1, -1, -1):
            right_pre[i] = running
            running *= nums[i]
        
        res = []
        for i in range(len(nums)):
            res.append(left_pre[i] * right_pre[i])
        
        return res
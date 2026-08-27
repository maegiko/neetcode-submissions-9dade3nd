class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [1] * len(nums)

        running = 1
        for num in nums:
            prefix.append(running)
            running *= num
        
        running = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = running
            running *= nums[i]
        
        res = []
        for i in range(len(prefix)):
            res.append(prefix[i] * suffix[i])

        return res
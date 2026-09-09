class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        res = []

        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                l_val = nums[l]
                r_val = nums[r]
                val = l_val + r_val

                if val < -(nums[i]):
                    while l + 1 < len(nums) and nums[l] == l_val:
                        l += 1
                elif val > -(nums[i]):
                    while r - 1 >= 0 and nums[r] == r_val:
                        r -= 1
                else:
                    triplet = [nums[l], nums[r], nums[i]]
                    res.append(triplet)
                    while l + 1 < len(nums) and nums[l] == l_val:
                        l += 1
                    
                    while r - 1 >= 0 and nums[r] == r_val:
                        r -= 1
            
            seen.add(nums[i])
        
        return res
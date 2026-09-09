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
                val = nums[l] + nums[r]

                if val < -(nums[i]):
                    l += 1
                elif val > -(nums[i]):
                    r -= 1
                else:
                    triplet = [nums[l], nums[r], nums[i]]
                    if triplet not in res:
                        res.append(triplet)
                    l += 1
                    r -= 1
            
            seen.add(nums[i])
        
        return res
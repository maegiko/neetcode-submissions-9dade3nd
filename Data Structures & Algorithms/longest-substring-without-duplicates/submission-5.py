class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        longest = 0
        left = 0
        right = 0

        while right < len(s):
            if s[right] not in count:
                count[s[right]] = right
            else:
                if count[s[right]] >= left:
                    left = count[s[right]] + 1
                
                count[s[right]] = right
            
            length = right - left + 1
            longest = max(longest, length)
            right += 1
        
        return longest
                    
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # This solution is buns
        count = {}
        l = 0
        length = 0
        longest = 0
        mostFrequent = 0

        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            
            mostFrequent = max(mostFrequent, count[s[r]])
            length = r - l + 1

            while length - mostFrequent > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    count.pop(s[l], None)
                l += 1
                length = r - l + 1
            
            longest = max(longest, r - l + 1)
        
        return longest
            
            
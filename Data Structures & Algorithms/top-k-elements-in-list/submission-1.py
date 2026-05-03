class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        mostFreq = []
        for i in range(0, k):
            maxKey = max(freq, key=lambda num: freq[num])
            mostFreq.append(maxKey)
            del freq[maxKey]

        return mostFreq
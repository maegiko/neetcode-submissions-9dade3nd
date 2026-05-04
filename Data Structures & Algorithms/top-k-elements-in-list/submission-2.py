class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        for key, val in freq.items():
            bucket[val].append(key)

        mostFreq = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                mostFreq.append(n)
                if len(mostFreq) == k:
                    return mostFreq

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack != [] and stack[-1][0] < temperatures[i]:
                val = stack.pop()
                res[val[1]] = i - val[1]
            
            stack.append([temperatures[i], i])
        
        return res
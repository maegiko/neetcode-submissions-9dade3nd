class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            pop_idx = float("inf")

            if stack and heights[i] < stack[-1][1]:
                while stack and stack[-1][1] > heights[i]:
                    idx, height = stack.pop()
                    width = i - idx
                    area = width * height
                    max_area = max(max_area, area)
                    pop_idx = idx
                
            if pop_idx != float("inf"):
                stack.append((pop_idx, heights[i]))
            else:
                stack.append((i, heights[i]))
        
        max_width = len(heights)
        while stack:
            idx, height = stack.pop()
            width = max_width - idx
            area = height * width
            max_area = max(max_area, area)
        
        return max_area

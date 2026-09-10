class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ml, mr = 0, len(matrix) - 1

        while ml <= mr:
            mid = (ml + mr) // 2

            if target > matrix[mid][0]:
                ml = mid + 1
            elif target < matrix[mid][0]:
                mr = mid - 1
            else: 
                return True
        
        if mr < 0:
            return False
        
        nl = 0
        nr = len(matrix[mr]) - 1

        while nl <= nr:
            mid = (nl + nr) // 2

            if target > matrix[mr][mid]:
                nl = mid + 1
            elif target < matrix[mr][mid]:
                nr = mid - 1
            else:
                return True
        
        return False
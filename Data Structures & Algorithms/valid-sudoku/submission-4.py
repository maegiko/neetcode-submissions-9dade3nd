class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = defaultdict(set)
        
        for i in range(0, 9):
            for j in range(0, 9):
                row_key = f"{i} row"
                col_key = f"{j} col"
                box_i = i // 3
                box_j = j // 3
                box_key = f"{box_i}, {box_j}"
                val = board[i][j]

                if val in seen[row_key] or val in seen[col_key] or val in seen[box_key]:
                    return False
                
                if val != '.':
                    seen[row_key].add(val)
                    seen[col_key].add(val)
                    seen[box_key].add(val)
        
        return True
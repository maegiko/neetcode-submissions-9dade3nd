class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = defaultdict(set)
        
        # rows check
        for i in range(0, 9):
            for j in range(0, 9):
                key = f"{i} row"
                val = board[i][j]

                if val in seen[key]:
                    return False
                
                if val != '.':
                    seen[key].add(val)

                small_i = i // 3
                small_j = j // 3

                key = f"{small_i}, {small_j}"

                if val in seen[key]:
                    return False
                
                if val != '.':
                    seen[key].add(val)
        
        for i in range(0, 9):
            for j in range(0, 9):
                print(f"index is ({j}, {i})")
                key = f"{i} col"
                val = board[j][i]
                print(f"val is {val}")

                if val in seen[key]:
                    return False
                
                if val != '.':
                    seen[key].add(val)
        
        return True
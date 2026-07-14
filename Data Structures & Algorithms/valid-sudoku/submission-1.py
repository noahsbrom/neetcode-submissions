class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dr = defaultdict(set)
        dc = defaultdict(set)
        dq = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                q = (r//3 * 3) + c//3
                if val in dr[r] or val in dc[c] or val in dq[q]:
                    return False
                
                dr[r].add(val)
                dc[c].add(val)
                dq[q].add(val)
        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize hash sets to track numbers we have already seen
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)  # Key will be a tuple: (row // 3, col // 3)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Empty cells (marked with ".") are ignored
                if val == ".":
                    continue
                
                # Check for duplicate in the current row
                if val in rows[r]:
                    return False
                
                # Check for duplicate in the current column
                if val in cols[c]:
                    return False
                    
                # Check for duplicate in the current 3x3 box
                box_coord = (r // 3, c // 3)
                if val in boxes[box_coord]:
                    return False
                
                # If unique, add the value to all three tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_coord].add(val)
                
        return True
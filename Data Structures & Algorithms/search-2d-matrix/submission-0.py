class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)
        n = len(matrix[0])
        
        def binarySearch(s: int, e: int) -> bool:
            # Base case: search range is invalid
            if s > e:
                return False
                
            mid = s + (e - s) // 2
            
            # Map the virtual 1D index back to 2D coordinates
            row = mid // n
            col = mid % n
            
            element = matrix[row][col]
            
            if element == target:
                return True
            elif element > target:
                return binarySearch(s, mid - 1)  # Search left half
            else:
                return binarySearch(mid + 1, e)  # Search right half

        # Initialize the search from virtual index 0 to (m * n) - 1
        return binarySearch(0, (m * n) - 1)
        
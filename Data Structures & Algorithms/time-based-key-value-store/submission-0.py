class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn't exist at all, return empty string
        if key not in self.store:
            return ""
            
        pairs = self.store[key]
        l, r = 0, len(pairs) - 1
        res = ""
        
        # Binary search for the closest timestamp <= target timestamp
        while l <= r:
            mid = l + (r - l) // 2
            
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]  # This is a valid candidate value
                l = mid + 1          # Try to find a larger valid timestamp
            else:
                r = mid - 1          # The timestamp is too large, look left
                
        return res
        

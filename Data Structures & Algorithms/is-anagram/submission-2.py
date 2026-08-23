class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        d1 = {}
        d2 = {}
        st = set()
        
        for s1 in s:
            st.add(s1)
            if s1 not in d1:
                d1[s1] = 0  # Fixed: Start at 0
            d1[s1] += 1
        
        for s1 in t:
            st.add(s1)
            if s1 not in d2:
                d2[s1] = 0  # Fixed: Start at 0
            d2[s1] += 1
        
        for s1 in st:
            # Fixed: Use .get() to avoid KeyError and compare cleanly
            if d1.get(s1, 0) != d2.get(s1, 0):
                return False
                
        return True

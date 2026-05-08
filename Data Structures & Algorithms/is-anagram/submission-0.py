class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c_s, c_t ={},{}
        for i in range(len(s)):
            c_s[s[i]] = 1 + c_s.get(s[i], 0)
            c_t[t[i]] = 1 + c_t.get(t[i], 0)
        return c_s == c_t

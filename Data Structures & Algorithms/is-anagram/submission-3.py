class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}
        st= set()

        for i in s:
            st.add(i)
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for i in t:
            st.add(i)
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] += 1

        for i in st:
            if d1.get(i, 0) != d2.get(i, 0):
                return False
        return True



        
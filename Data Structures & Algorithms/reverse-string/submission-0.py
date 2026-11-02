class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st = s[:len(s) - 1]
        for i in range(len(s) - 2, -1, -1):
            print(st)
            q = st.pop(-1)
            print(q)
            s.append(q) 
            s.pop(0)      
            print(s) 
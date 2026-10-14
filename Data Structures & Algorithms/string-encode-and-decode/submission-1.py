class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += str(len(i)) + "*" + i
        print(encoded)
        return encoded 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while(s[j] != "*"):
                 j += 1
            len_str = int(s[i:j])
            res.append(s[j + 1 : j + 1 + len_str])
            i = j + len_str + 1
        return res 
            

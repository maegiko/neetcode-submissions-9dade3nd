class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ''

        for s in strs:
            encoding += f"{str(len(s))}${s}"
        
        return encoding

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            chars = ''
            while s[i] != "$":
                chars += s[i]
                i += 1
            
            i += 1
            chars = int(chars)
            res.append(s[i:i + chars])

            i = i + chars

        return res


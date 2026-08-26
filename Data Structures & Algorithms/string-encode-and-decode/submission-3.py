class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for s in strs:
            encoding += str(len(s)) + f"${s}"
        
        return encoding


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            num_letters = ""

            while s[i] != "$":
                num_letters += s[i]
                i += 1
            
            i += 1
            letters = int(num_letters)
            end = i + letters

            res.append(s[i:end])
            i = end

        return res
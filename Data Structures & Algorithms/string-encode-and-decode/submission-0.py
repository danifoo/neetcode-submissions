class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            word = ""
            for char in string:
                word += f"{ord(char):03d}"
            encoded += word + "128"

        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []

        curString = ""
        for i in range(0, len(s), 3):
            if s[i: i + 3] == "128":
                decoded.append(curString)
                curString = ""
            else:
                curChar = int(s[i: i + 3])
                curString += chr(curChar)

        return decoded
        

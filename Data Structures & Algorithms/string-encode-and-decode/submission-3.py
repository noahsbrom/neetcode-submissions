class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            encoded.extend( [str(len(word)), '#', word] )
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []

        num_string = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                length = int(''.join(num_string))
                decoded.append(s[i+1:i+1+length])
                i += length + 1
                num_string.clear()

            else:
                num_string.append(s[i])
                i += 1
        return decoded 

            
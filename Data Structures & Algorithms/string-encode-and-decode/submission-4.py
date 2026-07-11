class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            encoded.extend( [str(len(word)), '#', word] )
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[i] != '#':
                i += 1
            
            # found '#' char, length is s[j:i]
            length = int(s[j:i])
            decoded.append(s[i+1:i+1+length])
            i += length + 1
        return decoded 

            
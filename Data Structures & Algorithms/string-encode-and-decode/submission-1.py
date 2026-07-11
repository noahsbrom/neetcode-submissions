class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            for c in word:
                encoded.extend([c, c])
            encoded.append('./')
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        cur = []

        i = 0
        for i in range(0, len(s), 2):
            if s[i] == '.' and s[i+1] == '/':
                decoded.append(''.join(cur))
                cur = []
            else:
                cur.append(s[i])
                i += 2
        return decoded
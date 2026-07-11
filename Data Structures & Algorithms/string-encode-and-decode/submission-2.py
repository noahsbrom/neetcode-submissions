class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            encoded.extend( [str(len(word)), '#'] )
            for c in word:
                encoded.append(c)
        print(''.join(encoded))
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        cur = []

        num_string = []
        length_remaining = 0
        for c in s:
            if length_remaining > 0:
                cur.append(c)
                length_remaining -= 1
                if length_remaining == 0:
                    decoded.append(''.join(cur))
                    cur.clear()
            else:
                if c.isdigit():
                    num_string.append(c)
                if c == '#':
                    length_remaining = int(''.join(num_string))
                    if length_remaining == 0:
                        decoded.append('')
                    num_string.clear()
        return decoded
                    

            
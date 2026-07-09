class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_counts = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            letter_counts[index] += 1
        
        for char in t:
            index = ord(char) - ord('a')
            letter_counts[index] -= 1
        
        for count in letter_counts:
            if count != 0:
                return False
        return True


        
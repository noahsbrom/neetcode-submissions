class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_counts = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            letter_counts[index] += 1
        
        for char in t:
            index = ord(char) - ord('a')
            letter_counts[index] -= 1
        
        return all(count == 0 for count in letter_counts)


        
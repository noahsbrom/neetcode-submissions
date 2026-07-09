class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_counter = Counter(s)
        for t_ch in t:
            if t_ch not in c_counter:
                return False
            c_counter[t_ch] -= 1
        
        # anagram -> count diff for all chars between s and t is 0
        for diff in c_counter.values():
            if diff != 0:
                return False
        return True

        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        longest = 0
        seen = set()
        left = right = 0
        while right < n:
            while left < right and s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, len(seen))
            right += 1
        return longest
            



        
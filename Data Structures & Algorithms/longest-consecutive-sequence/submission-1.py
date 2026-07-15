class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if num-1 not in s:
                cur = 1
                next_num = num+1
                while next_num in s:
                    cur += 1
                    next_num += 1
                longest = max(longest, cur)
        return longest
    
    




        
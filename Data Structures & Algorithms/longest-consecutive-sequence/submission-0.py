class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        starting_nums = []
        for num in s:
            if num-1 not in s:
                starting_nums.append(num)
        
        longest = 0
        for starting_num in starting_nums:
            cur = 1
            next_num = starting_num+1
            while next_num in s:
                cur += 1
                next_num += 1
            longest = max(longest, cur)
        return longest




        
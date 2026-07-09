class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # v1 + v2 = target -> v1 = target - v2
        d = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in d:
                # d[diff] will always be smaller index since it was already seen
                return [d[diff], i]
            # don't need to check for existence since only one pair satisfy condition
            d[num] = i
        
        # assume every input has solution
        
                
        
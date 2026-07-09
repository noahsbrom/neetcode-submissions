class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # v1 + v2 = target -> v1 = target - v2
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                # d[target-num] will always be smaller index since it was already seen
                return [d[target-num], i]
            
            if num not in d:
                d[num] = i
        
        # assume every input has solution
        
                
        
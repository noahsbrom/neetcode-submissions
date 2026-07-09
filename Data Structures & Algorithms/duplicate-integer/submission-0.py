class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        determine if input array has duplicate

        args:
            nums (List[int]) - input array to check

        returns:
            bool: true if any value appears more than once in nums, false otherwise
        """

        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
        



        
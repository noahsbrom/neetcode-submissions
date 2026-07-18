class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        nums.sort()

        n = len(nums)
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum == 0:
                    arr = [nums[i], nums[j], nums[k]]
                    if arr not in ans:
                        ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif cur_sum > 0:
                    k -= 1
                else:
                    j += 1
        return ans

        
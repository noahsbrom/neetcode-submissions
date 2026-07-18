class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        nums.sort()

        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break
            # skip duplicates and i values whose max triplet is negative
            if (i > 0 and nums[i] == nums[i-1]) or (nums[i] + nums[n-1] + nums[n-2] < 0):
                continue

            j = i + 1
            k = n - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif cur_sum > 0:
                    k -= 1
                else:
                    j += 1
        return ans

        
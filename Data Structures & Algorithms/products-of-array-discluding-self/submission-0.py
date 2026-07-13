class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        postfix_products = [1] * (n+1)
        for i in range(n-1, -1, -1):
            postfix_products[i] = nums[i] * postfix_products[i+1]
        
        output = []
        running_product = 1
        for i in range(n):
            output.append(running_product * postfix_products[i+1])
            running_product *= nums[i]
        
        return output




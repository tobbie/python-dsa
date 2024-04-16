class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        result =  [1] * len(nums)
        endIndex = len(nums) - 1
        
        prefix[0] *= nums[0]
        for index in range(1, len(nums)):
            prefix[index] = prefix[index -1] * nums[index]
        
        postfix[endIndex] *= nums[endIndex]
        for index in range(len(nums) -2, -1, -1):
            postfix[index] = postfix[index +1] * nums[index]
        
        print(prefix)
        print(postfix)

        result[0] *= postfix[1]
        result[endIndex] *= prefix[endIndex -1]

        for index in range(1, len(nums) -1):
            result[index] = prefix[index -1 ] * postfix[index +1]
        
        print(result)

    
    
sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
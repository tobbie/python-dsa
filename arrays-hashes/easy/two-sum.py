class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:  
        tracker = {}     
        for index in range(len(nums)):
            difference = target - nums[index] 
           
            if difference in tracker:              
                return [tracker[difference], index]
               # add number at current index to array
            tracker[nums[index]] = index
    
        return []









class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:  
        tracker = {}
        result = []

        for index in range(len(nums)):
            difference = target - nums[index] 
           
            if tracker.get(difference, -1) == -1:              
                tracker[nums[index]] = index 
            else:    # we found the two numbers
                result.append(tracker[difference]) # append index of current difference
                result.append(index)   # append index of current array value
    
        return result
    



sol = Solution2()
result = sol.twoSum([3, 3], 6)
print(result)

            
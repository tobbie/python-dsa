class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequencyTable = {}
        bucket = [[] for i in range(len(nums) + 1)]
        result = []
        #build frequency table
        for num in nums:
            frequencyTable[num] = 1 + frequencyTable.get(num, 0)
        
        #add keys of frequency table to buket list using values as index
        for key, value in frequencyTable.items():
            bucket[value].append(key)
        
     
       
        for index in range(len(bucket) - 1, 0, -1):
            for item in bucket[index]:
                result.append(item)
                if len(result) == k:
                    return result
        
        return result



def main():
    sol = Solution()
    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(sol.topKFrequent([3, 0, 1, 0], 1))

main()

        
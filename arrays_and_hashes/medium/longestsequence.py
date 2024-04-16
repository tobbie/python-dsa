from collections import defaultdict

# Space time complexity  O(n) time and O(n) space

class LongestSequence:
    def longestConsecutive(self, nums: list[int]) -> int:
        hashMap = defaultdict(list)

        for num in nums:
            hashMap[num] = False
        
        longest = 0
        for num in nums:
            nextNum = num + 1
            currentLength = 1
            while hashMap.get(nextNum, 0) is not 0 and hashMap[nextNum] == False:  # number exists and it has not been visited 
                currentLength += 1
                hashMap[nextNum] = True
                nextNum += 1
            
            prevNum = num -1

            while hashMap.get(prevNum, 0) is not 0 and hashMap[prevNum] == False: # number exists and it has not been visited
                currentLength += 1
                hashMap[prevNum] = True
                prevNum -= 1

            longest = max(longest, currentLength)

        
        return longest
            

            

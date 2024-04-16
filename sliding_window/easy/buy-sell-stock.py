class Solution:
    #O(n) time , O(1) space
    def maxProfit(self, prices: list[int]) -> int:
        leftPointer, rightPointer = 0 , 1
        maxProfit = 0

        while(rightPointer < len(prices)):
            if(prices[rightPointer] > prices[leftPointer]):
                profit = prices[rightPointer] - prices[leftPointer]
                maxProfit = max(maxProfit, profit)
            else:
                leftPointer = rightPointer
            
            rightPointer += 1
        
        return maxProfit
    


def main():
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6, 4, 3, 1]))

main()

    

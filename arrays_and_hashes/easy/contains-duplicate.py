
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)

        return False


def main():
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,1]))
    print(sol.containsDuplicate([1,2,3,4, 5, 6]))
    print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
    

main()
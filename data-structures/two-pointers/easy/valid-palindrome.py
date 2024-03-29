class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_array = []
        for index in range(len(s)):
           if not s[index].isalnum():
               continue
           char_array.append(s[index].lower())

        
        left = 0 
        right = len(char_array) -1

        while(left < right):
            if char_array[left] != char_array[right]:
                return False
            left +=1
            right -= 1
        
        return True
    

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        dictA, dictB = {}, {}

        for index in range(len(s)):
            dictA[s[index]] = 1 + dictA.get(s[index], 0)
            dictB[t[index]] = 1 + dictB.get(t[index], 0)

        
        for key in dictA:
            if dictA[key] != dictB.get(key, 0):  # if you find that the  frquency of a character in the dictionaries are not the same or that a character does not  exist in the other return false
                return False
        
        return True  # if we get here, then both strings are anagrams.
            

def main():
    sol = Solution()
    print(sol.isAnagram("tar", "rat"))
    print(sol.isAnagram("cat", "tac"))
    print(sol.isAnagram("par", "rat"))
    print(sol.isAnagram("parr", "rat"))

main()
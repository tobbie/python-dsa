from collections import defaultdict

# time O(m * n)
class Solution2:
    def groupAnagrams(self, word_list: list[str]) -> list[list[str]]:
        result = defaultdict(list)

        for word in word_list:
            char_list = [0] * 26 # a - z
            for character in word:
                char_list[ord(character) - ord("a")] += 1   #finds the index posiiton of a lower case character in the list
            
            result[tuple(char_list)].append(word)
        
        return result.values()



# O(nlogn) * m
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)  # initialize dict like this so you won't have to write code to check if a key already exists

        for word in strs:
            sorted_word = self.__sort_word(word)
            result[sorted_word].append(word)
            
        return result.values()
    

    def __sort_word(self, item):
        word_list = list(item)
        word_list.sort()
        return ''.join(word_list)



def main():
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

main()
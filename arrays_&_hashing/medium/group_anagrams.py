from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # use frequencies as base logic. anagram is just frequency of each char is same
        anagram_dict = defaultdict(list)

        for word in strs:

            # create an array of size 26, increment char and take that as key
            key = [0]*26
            for char in word:
                key[ord(char) - ord('a')] += 1
            
            # keys must be hashable so convert key list it to tuple
            key = tuple(key)
            anagram_dict[key].append(word)
  
        return list(anagram_dict.values())
        
    """
    Question: https://leetcode.com/problems/group-anagrams/
    Time complexity: O(n*m), n is the number of strings and m is the length of the longest string.
    Space complexity: O(n * m), for storing the anagrams in the dictionary."""
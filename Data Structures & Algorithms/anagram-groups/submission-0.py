"""
@u
Input(s): 1 array of strings: strs
output(s): array of arrays

Example(s):
1. Input: strs=["act", "pots", "tops", "cat", "stop", "hat"]
Output: res=[["pots", "tops", "stop"], ["cat", "act"], ["hat"]]

- We know that pots, tops, and stop are anagrams because they have the same frequency of characters. 
- We count them, p:1, o:1, t:1, s:1
- How do we associate the frequency of characters to a grouped anagram? 
    - What if we sort the string itself? 
    - If we sort the string itself, do we even need to count the frequency? 
@m

@p
BF/
1. For loop: For each string, we send into subfunction called classify() -> count the frequency of each character from the string that is passed in
2. Dictionary to keep track of grouped anagrams. What will be our key? What will be our value? 
2a. What if we use the sorted anagram as the key, and the value will be an array that contains all anagrams of the string.
2b. This way, we can return the result as the dictionary values by appending it to a list. 
TC: O(nlogn) [Sorting the anagram] + O(n) [Traversing the strs array]

Approach 2/
1. For loop: For each string in inside strs, we are going to send into a subfn called classify(string)
2. classify(string): sort the input string to identify if it belongs with an exisiting group or a new group // O(nlogn) * O(n)
3. Dictionary will have keys as the sorted anagram and values as arrays of other valid anagrams

TC:
SC:
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} 
        ans = []
        def classifyWord(word):
            sorted_word = sorted(word)
            sorted_word = ''.join(sorted_word)
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]

        
        for i in range(len(strs)):
            word = strs[i]
            classifyWord(word)

        for key, values in anagrams.items():
            ans.append(values)
        return ans
            
    


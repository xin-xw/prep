"""
@u
What is an anagram? An anagram is an english word where the string contains the exact same characters as another string, but the ordering of the characters can be different.
What are we testing for here? We are testing for and caring for frequency of each character between two strings.
Between two strings, s and t, they must contain the exact amount of characters and its frequency.

1. Both s and t must be equal length.
2. Can I assume s and t will only contain english characters?
3. Case sensitivity?

Input(s): s, t: strings
output(s): boolean -> True if both s and t are valid anagrams, False otherwise

Example(s):
1.
s: "teapot"
t: "eattop"
Output: T, T: 2, E: 1, A: 1, O: 1

2.
s: "racecar"
t: "racccar"
Output: False

@m
BF/
1. Iterate through string s, with associated dictionary s_dict, that keeps track of frequency and count of characters as we traverse through s.
2. When we iterate through string t, we validate two things: 1) if the current element is not in our s_dict, then we return False; 2) if the current elt. is in s_dict, subtract frequency by 1
3. All dictionary values should have frequency of 0, otherwise we return False.
4. If the strings s,t are of different lengths, return False. -> Make this first step so it's an O(1) exit.

@p

@i

@r

TC:
SC:
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_dict = {}

        for i in range(len(s)):
            cur_elt = s[i]
            if cur_elt not in s_dict:
                s_dict[cur_elt] = 1
            else:
                s_dict[cur_elt] += 1
        
        for i in range(len(t)):
            cur_elt = t[i]
            if cur_elt not in s_dict:
                return False
            else:
                s_dict[cur_elt] -= 1
        
        for key, values in s_dict.items():
            if values != 0:
                return False

        return True

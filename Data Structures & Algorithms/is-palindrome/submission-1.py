"""
@understand
input: string s
output: boolean: True if s is a palindrome, False otherwise

Palindrome: a string that reads the same forward and backward. It is case-insensitive. It ignores all non-alphanumeric characters.

Alphanumeric character: A-Z, a-z, 0-9 -> only characters that are considered

* Spaces are ignored

ex1: input: asdfdsa output: True
ex2: input: asdffdsa output: True
ex3: input: assdfsa output: False

@match
1. Remove all spaces from s, or if a space is detected then we skip
2. When considering palindromes, the most important thing is comparing and ensuring the beginning character and the end character are matched. In the case they aren't the same -> Return False.
3. If the string (after spaces are removed) is odd -> We ignore the middle character, because it'll be the same from both ways. 
4. If the string (after spaces are removed) is even -> We proceed with the algo. because must make sure the middle two characters are palindromic. 

Two pointers

@plan
1. Remove spaces from a string
2. Two Pointers, with one at each end of the string

TC: O(n)
SC: O(n)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        cleaned = ""
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        left = 0
        right = len(cleaned)-1

        
        while left <= right:
            if cleaned[left] == cleaned[right]:
                left += 1
                right -= 1
            else:
                return False
        return True



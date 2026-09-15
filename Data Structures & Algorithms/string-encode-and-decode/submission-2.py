"""
@u
we are to design two algorithms: 1) encode(), which takes in a list of strings ["", "", ""] and returns 1 string; 2) decode(), which takes in the encoded string and returns the list of string

in order to complete this task, there has to be a separator that we are using to help us to concatenate the string that is invisible to the end user -> .join() in python maybe?

@m
machine 1 

encoded_string = encode(arr)

    ex: arr = ["1", "2", "3"]
    when I call encode(arr), i want the result to be 1u2u3u, and when I call decode(1u2u3u), I want the result to be ["1", "2", "3"], assuming that my concatenation is joined by the character u.

* Problem
    - There can always be a possibility that the concatenation character I am using is within the string itself. 
        - To prevent this, think backwards from the decode() function, how do we have a guaranteed way to identify the next string? 
            - If we are to include the length of the string before we decode it, then we are to know how long the next string is -> i.e. 3[length]abc[string]. 
            * Problem
                - What if the string itself also includes an integer?
                    - That is when the delimiter comes in handy

@p
encode() function utilizes two distincts to help encode all the strings together: 1) integer: length of string, followed right by 2) delimiter character. These two distincts allow the decode() function to identify exactly how to separate and delimit the strings

1. encode(strs: List[str]):
    # for each string s, the work is: 1) compute the length of s, and 2) copy s to a separate result string that we are to append.
    # because the length of s varies, we are to assume the TC of encode to be O(len(s1) + len(s2) + len(s3) + ...) ? 
    # for each s in strs:
        calculate length of each s 
            and create result string by appending length + delimiter character
                temp_result = length + delimiter + s
    result += temp_result
    

2. decode(s)
    # take in the result string 
    # because we know what the delimit character is and how the algorithm works, we do a for loop and we do a for loop to scan for the full integer first and this scan ends when we hit the delimiter character

    # afterwards we can do another for loop running for integer length to extract the string starting from the delimiter character


"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        delimiter = "#"
        res = ""
        
        for i in range(len(strs)):
            separated_str = strs[i]
            temp_res = str(len(separated_str)) + delimiter + separated_str
            res += temp_res
        
        return res


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        def extractstring(start, s, length):
            extracted_string = ""
            new_starting_position = start + length
            
            for k in range(start, start + length):
                extracted_string += s[k]
            return extracted_string, new_starting_position
            
        
        delimiter = "#"
        calculated_length = 0
        res = []
        i = 0
        while i < len(s):
            calculated_length = ""
            while s[i] != delimiter: # afraid of out of bounds? 
                                     # until we hit the delimiter, ...
                calculated_length += s[i] # we wawnted to append the stringed integer to our calculated_length variable
                i += 1 # increment i 

            calculated_length = int(calculated_length) # turn it into an actual integer to use
            extracted_string, i = extractstring(i+1, s, calculated_length)
            res.append(extracted_string)

        return res

        





class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        if len(digits) == 0:
            return []
        output = phone[digits[0]]
        
        for c in digits[1:]:
            output = [a+b for a in output for b in phone[c]]
        return output

"""
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]
"""

s = Solution()
s.letterCombinations("23")
s.letterCombinations("")
s.letterCombinations("2")
s.letterCombinations("234")




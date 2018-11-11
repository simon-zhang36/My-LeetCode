class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: ool
        """
        parentheses_lookup = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c in parentheses_lookup:
                stack.append(c)
            elif stack == [] or parentheses_lookup[stack.pop()] != c:
                return False
        return stack == []

if __name__ == "__main__":
    print(Solution().isValid("{[]}"))
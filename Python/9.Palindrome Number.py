class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False
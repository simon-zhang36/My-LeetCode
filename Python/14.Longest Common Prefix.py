class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        longest = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(s) and i < len(longest) and s[i] == longest[i]:
                i += 1
            longest = longest[:i]
        return longest

if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        str = str.lstrip()
        newstr = ""
        for i in range(len(str)):
            if "0" <=str[i] <= "9" or (str[i] in ("+","-") and i == 0):
                newstr += str[i]
            else:
                break
        if newstr in ("","+","-"):
            return 0
        elif -2147483648 <= int(newstr) <= 2147483647:
            return int(newstr)
        elif int(newstr) < -2147483648:
            return -2147483648
        elif int(newstr) > 2147483647:
            return 2147483647
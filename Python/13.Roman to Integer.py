class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        roman_numeral_dictionary = (('M',  1000),('CM', 900),('D',  500),('CD', 400),('C',  100),('XC', 90),('L',  50),('XL', 40),('X',  10),('IX', 9),('V',  5),('IV', 4),('I',  1))
        
        index,Number = 0,0
        for roman,num in roman_numeral_dictionary:
            while s[index:index + len(roman)] == roman:
                Number += num
                index += len(roman)
        return Number
                
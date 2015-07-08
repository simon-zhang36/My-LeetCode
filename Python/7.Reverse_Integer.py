class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x < 0:
            y = str(x)[::-1]
            y = int("-" + y[:-1])
            
        if x >= 0:
            y = int(str(x)[::-1])
        # if abs(y) >= sys.maxint           
        if abs(y) >= 2147483647: 
            return 0
        else:
            return y
            
         
if __name__ == "__main__":
    print Solution().reverse(1235)
    print Solution().reverse(-321234)
    


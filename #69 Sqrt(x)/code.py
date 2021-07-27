class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        flag = False
        while flag is not True:
            if i*i <= x and (i+1)*(i+1) > x:
                return i
                flag = True
            else:
                i +=1
            
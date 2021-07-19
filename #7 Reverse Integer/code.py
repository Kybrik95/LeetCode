class Solution:
    def reverse(self, x: int) -> int:
        reversed_x = ''
        if x < 0:
            sign = '-'
            x = str(x)[1:]
        else:
            sign = ''
            x = str(x)
        reversed_x = reversed_x.join(reversed(x))
        x = int(sign + reversed_x)
        print(x)
        if x < -2**31 or x > 2**31 - 1:
            return 0
        else:
            return x
        
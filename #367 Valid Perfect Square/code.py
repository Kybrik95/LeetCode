class Solution:
    def isPerfectSquare(self, x: int) -> bool:
        eps = 0.99
        if x == 0:
            x_next = 0
        else:
            x_curr = x
            x_next = 0
            while 42:
                x_next = (x_curr + x / x_curr) / 2
                if abs(x_next - x_curr) <= eps:
                    break
                else:
                    x_curr = x_next
        if int(x_next) * int(x_next) != x:
            return False
        else:
            return True

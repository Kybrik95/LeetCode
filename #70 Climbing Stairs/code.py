class Solution:
    def climbStairs(self, n: int) -> int:
        fib1 = fib2 = 1
        for i in range(1, n):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2


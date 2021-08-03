class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_x = ''
        if x < 0:
            is_palindrome = False
        else:
            x = str(x)
            if len(x) % 2 != 0:
                median_index = (len(x) + 1) / 2
            else:
                median_index = (len(x) / 2)
            reversed_x = reversed_x.join(reversed(x))
            return reversed_x[0:int(median_index)] == x[0:int(median_index)]

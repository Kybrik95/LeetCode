# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        mid = (start + end)//2
        while end != start:
            if isBadVersion(mid):
                end = mid 
            else:
                start = mid + 1
            mid = (start + end)//2
        return mid

            
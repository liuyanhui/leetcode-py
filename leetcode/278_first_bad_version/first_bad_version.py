"""
https://leetcode.com/problems/first-bad-version/
278. First Bad Version
Easy
-------------
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:
Given n = 5, and version = 4 is the first bad version.
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        验证通过:
        Runtime: 28 ms, faster than 71.50% of Python3 online submissions for First Bad Version.
        Memory Usage: 13.7 MB, less than 6.90% of Python3 online submissions for First Bad Version.
        :type n: int
        :rtype: int
        """

        def isBadVersion(m):
            return True if m >= 4 else False

        if n <= 0:
            return 0
        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l if isBadVersion(l) else 0


def main():
    ret = Solution().firstBadVersion(8)
    print(ret)
    print(ret == 4)
    print('--------------------')

    ret = Solution().firstBadVersion(1000)
    print(ret)
    print(ret == 4)
    print('--------------------')

    ret = Solution().firstBadVersion(1)
    print(ret)
    print(ret == 0)
    print('--------------------')

    ret = Solution().firstBadVersion(2)
    print(ret)
    print(ret == 0)
    print('--------------------')


if __name__ == "__main__":
    main()

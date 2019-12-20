"""
https://leetcode.com/problems/largest-perimeter-triangle/
976. Largest Perimeter Triangle
Easy
------------------------
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.
If it is impossible to form any triangle of non-zero area, return 0.
Example 1:
Input: [2,1,2]
Output: 5

Example 2:
Input: [1,2,1]
Output: 0

Example 3:
Input: [3,2,3,4]
Output: 10

Example 4:
Input: [3,6,2,3]
Output: 8

Note:
3 <= A.length <= 10000
1 <= A[i] <= 10^6
"""


class Solution:
    def largestPerimeter(self, A):
        return self.largestPerimeter_1(A)

    def largestPerimeter_1(self, A):
        """
        1.排序
        2.从大到小计算三角形周长,第一个符合条件的三角形就是所求
        ----------------
        验证通过,性能不错:
        Runtime: 208 ms, faster than 84.00% of Python3 online submissions for Largest Perimeter Triangle.
        Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Largest Perimeter Triangle.
        :param A:
        :return:
        """
        if A is None and len(A) < 3:
            return 0
        ret = 0
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                ret = A[i] + A[i + 1] + A[i + 2]
                break
        return ret


def main():
    n = [2, 1, 2]
    ret = Solution().largestPerimeter(n)
    print(ret)
    print(ret == 5)
    print("--------------------")

    n = [1, 2, 1]
    ret = Solution().largestPerimeter(n)
    print(ret)
    print(ret == 0)
    print("--------------------")

    n = [3, 2, 3, 4]
    ret = Solution().largestPerimeter(n)
    print(ret)
    print(ret == 10)
    print("--------------------")

    n = [3, 6, 2, 3]
    ret = Solution().largestPerimeter(n)
    print(ret)
    print(ret == 8)
    print("--------------------")

    n = [3, 6, 2, 3,111,23,445,443,212]
    ret = Solution().largestPerimeter(n)
    print(ret)
    print(ret == 8)
    print("--------------------")


if __name__ == "__main__":
    main()

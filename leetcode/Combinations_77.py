"""
77. Combinations
Medium
---------------------------
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:
1 <= n <= 20
1 <= k <= n
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combine_1(n, k)

    def combine_1(self, n: int, k: int) -> List[List[int]]:
        """
        Round 3
        Score[4] Lower is harder

        Thinking：
        1. 递归思路
        helper(n:int,beg:int,k:int)

        验证通过：
        Runtime 859 ms Beats 10.65%
        Memory 64.78 MB Beats 67.54%
        """
        ret = []

        def helper(beg: int, k: int, seen: list):
            if k <= 0:
                return ret.append(seen.copy())
            for i in range(beg, n + 1):
                seen.append(i)
                helper(i + 1, k - 1, seen)
                seen.remove(i)

        helper(1, k, [])
        return ret


def do_func(n: int, k: int, expect: list):
    ret = Solution().combine(n, k)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func(n=4, k=2, expect=[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
    do_func(n=1, k=1, expect=[[1]])


if __name__ == "__main__":
    main()

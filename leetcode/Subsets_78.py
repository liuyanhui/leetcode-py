"""
78. Subsets
Medium
-------------------------------
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subsets_1(nums)

    def subsets_1(self, nums: List[int]) -> List[List[int]]:
        """
        Thinking：
        1. 递归。找出从0~n的所有组合。
        遍历每个数字，每次遍历选择一个数字，然后递归，公式如下：
        helper(nums,k) = i + helper(nums excludes i,k-1), for i in nums


        验证通过：
        Runtime 34 ms Beats 78.07%
        Memory 16.65 MB Beats 81.60%
        """
        ret = []

        def helper(nums: List[int], k: int, beg: int, cache: List[int]):
            if k <= 0:
                return ret.append(cache.copy())
            for i in range(beg, len(nums)):
                cache.append(nums[i])
                helper(nums, k - 1, i + 1, cache)
                cache.remove(nums[i])
                # review 可以替换上一行代码 cache.pop()

        for i in range(len(nums) + 1):
            helper(nums, i, 0, [])
        return ret


def do_func(nums: List[int], expect: List[List[int]]):
    ret = Solution().subsets(nums)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    do_func([0], [[], [0]])


if __name__ == "__main__":
    main()

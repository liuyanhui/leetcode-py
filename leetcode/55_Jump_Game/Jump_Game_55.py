"""
55. Jump Game
Medium
-------------------------
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""


class Solution:
    def canJump(self, nums: list) -> bool:
        return self.canJump_1(nums)

    def canJump_1(self, nums: list) -> bool:
        """
        Round 3
        Score[4] Lower is harder

        Thinking：
        1. BFS思路
        1.1. 依次计算nums中的每个元素，记录其最远可达的下标end，当end大于等于len(nums)-1时，返回True。
        1.2. IF end<i THEN return False
        1.3. 本题采用BFS思路
        2. DP思路
        2.1. DP思路是BFS思路的反转.参见leetcode-java.

        验证通过:
        382 ms Beats 84.57%
        18.68 MB Beats 21.26%

        Args:
            nums:

        Returns:

        """
        end = 0
        for i in range(len(nums)):
            # 中途不满足条件的情况
            if 0 < i and end < i:
                return False
            end = max(end, i + nums[i])
            # 最终满足条件
            if end >= len(nums) - 1:
                return True

        return False


def do_func(nums: list, expect: bool):
    ret = Solution().canJump(nums)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func([2, 3, 1, 1, 4], True)
    do_func([3, 2, 1, 0, 4], False)
    do_func([3, 2, 1, 1, 4], True)


if __name__ == '__main__':
    main();

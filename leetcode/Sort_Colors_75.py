"""
75. Sort Colors
Medium
----------------------------------
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""


class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.sortColors_1(nums)

    # review Dutch National Flag Problem
    def sortColors_1(self, nums: list) -> None:
        """
        Round 3
        Score[3] Lower is harder

        Thinking：
        1. 貌似是荷兰三色旗问题
        2. naive solution。排序法。
        Time Complexity:O(NlogN)
        Space Complexity:O(1)
        3. 两次遍历法（双指针遍历）。
        3.1. 第一次从左向右遍历，把0移动到左侧；第二次从右向左遍历，把2移动到右侧。
        3.2. 第一次遍历时：[0:l]表示全是0，(l,r)是已计算的非0部分，[r:~]是未计算的部分。
        3.3. 第一次遍历。遍历nums
        IF nums[i]==0 THEN swap(l,i),l++,i++
        IF nums[l]!=0 THEN i++
        3.4.
        Time Complexity:O(2N)
        Space Complexity:O(1)
        4. One-pass，分段法。
        在计算过程中，0移动到最左侧，2移动到最右侧，剩下的都是1。
        假设：m = len(list) ,l=0,r=m-1。
        [0:l)全是0的部分，[l,i)全是1的部分，[i,r]待计算的部分，(r,~]全是2的部分。
        4.1. 遍历nums
        IF nums[i]==0 THEN swap(l,i),l++,i++
        IF nums[i]==1 THEN i++
        IF nums[i]==2 THEN swap(i,r),r--
        4.2.
        Time Complexity:O(N)
        Space Complexity:O(1)

        本方法采用4.
        还有一种two-pass思路:第一次pass统计0,1,2出现的次数,第二次pass重写数组

        验证通过:
        Runtime 31 ms Beats 91.66%
        Memory 16.43 MB Beats 93.15%
        """
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1


def do_func(nums: list, expect: list):
    Solution().sortColors(nums)
    print(nums)
    print(nums == expect)
    print("---------------------")


def main():
    do_func([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2])
    do_func([2, 0, 1], [0, 1, 2])


if __name__ == "__main__":
    main()

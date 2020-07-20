"""
https://leetcode.com/problems/3sum-smaller/
https://www.cnblogs.com/jcliBlogger/p/4736809.html
259. 3sum_smaller
Medium
-----------
Problem Description:
Given an array of n integers nums and a target,
find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.
Return 2.
Because there are two triplets which sums are less than 2:
[-2, 0, 1]
[-2, 0, 3]

Follow up:
Could you solve it in O(n^2) runtime?
"""


class Solution:
    def three_sum_smaller(self, nums, target):
        return self.three_sum_smaller_binary_search(nums, target)

    def three_sum_smaller_binary_search(self, nums, target):
        """
        binary search 方法,在three_sum_smaller_two_point()的基础上改造而成.
        主要修改的地方为:步骤三中的双指针夹逼法改为二分查找法
        时间复杂度:O(N*N*logN)
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) == 0:
            return 0
        count = 0
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # binary searh 找到3sum小于target的最大下标k
                l, r = j + 1, len(nums) - 1
                tmp = j
                while l <= r:
                    mid = (l + r) // 2
                    if nums[i] + nums[j] + nums[mid] >= target:
                        r = mid - 1
                    else:
                        tmp = mid
                        l = mid + 1
                k = tmp - j
                count += k

        return count

    def three_sum_smaller_two_point(self, nums, target):
        """
        双指针夹逼法.
        步骤如下:
        1.数组排序
        2.遍历nums,并将问题转化为two sum smaller问题
        3.基于步骤2,使用双指针夹逼法.
            if nums[i]+nums[l]+nums[r]>=target : r-=1
            else : l+=1 count+=1
        4.返回count
        时间复杂度:O(N*N)
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) == 0:
            return 0
        count = 0
        nums.sort()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] >= target:
                    r -= 1
                else:
                    count += (r - l)
                    l += 1
        return count

    def three_sum_brute(self, nums, target):
        """
        暴力法.
        Time Complexity:O(N**3)
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) == 0:
            return 0
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] < target:
                        count += 1
        return count


def main():
    nums = [-2, 0, 1, 3]
    target = 2
    ret = Solution().three_sum_smaller(nums, target)
    print(ret)
    print(ret == 2)
    print('--------------------')


if __name__ == "__main__":
    main()

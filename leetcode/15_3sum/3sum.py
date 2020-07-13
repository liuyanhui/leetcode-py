"""
https://leetcode.com/problems/3sum/
15. 3Sum
Medium
-------------------------
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        return self.threeSum_3(nums)

    def threeSum_3(self, nums):
        """
        不用递归法,
        threeSum_2的改进版本,只是添加了去重逻辑
        验证通过:
        Runtime: 1392 ms, faster than 35.76% of Python3 online submissions for 3Sum.
        Memory Usage: 17.2 MB, less than 66.87% of Python3 online submissions for 3Sum.
        :param nums:
        :return:
        """
        if not nums or len(nums) == 0:
            return []
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return ret

    def threeSum_2(self, nums):
        """
        不用递归法,
        验证失败,
        Time Limit Exceeded:311 / 313 test cases passed.
        :param nums:
        :return:
        """
        if not nums or len(nums) == 0:
            return []
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    tmp = [nums[i], nums[l], nums[r]]
                    if tmp not in ret:
                        ret.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return ret

    def threeSum_1(self, nums):
        """
        思路:NSum问题通用解决思路,采用递归法
        时间复杂度 O(N*N)
        验证超时,
        Time Limit Exceeded::311 / 313 test cases passed.
        :param nums:
        :return:
        """
        if not nums or len(nums) == 0:
            return []
        ret = []

        def findNSum(n, t, N, beg, cache):
            if N == 2:
                l, r = beg, len(n) - 1
                while l < r:
                    if n[l] + n[r] == t:
                        tmp = cache + [n[l], n[r]]
                        if tmp not in ret:
                            ret.append(tmp)
                        l += 1
                        r -= 1
                    elif n[l] + n[r] > t:
                        r -= 1
                    else:
                        l += 1
                return
            for i in range(beg, len(n)):
                findNSum(n, t - n[i], N - 1, i + 1, cache + [n[i]])

        nums.sort()
        findNSum(nums, 0, 3, 0, [])
        return ret


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    ret = Solution().threeSum(nums)
    ret.sort()
    ret.reverse()
    print(ret)
    print(ret == [
        [-1, 0, 1],
        [-1, -1, 2]
    ])
    print("---------------------")

    nums = [0, 0, 0, 0, 0]
    ret = Solution().threeSum(nums)
    ret.sort()
    ret.reverse()
    print(ret)
    print(ret == [
        [0, 0, 0]
    ])
    print("---------------------")

    nums = [6, -5, -6, -1, -2, 8, -1, 4, -10, -8, -10, -2, -4, -1, -8, -2, 8, 9, -5, -2, -8, -9, -3, -5]
    ret = Solution().threeSum(nums)
    ret.sort()
    ret.reverse()
    print(ret)
    print(ret == [[-10,4,6],[-8,-1,9],[-6,-3,9],[-6,-2,8],[-5,-4,9],[-5,-3,8],[-5,-1,6],[-4,-2,6],[-3,-1,4],[-2,-2,4]])
    print("---------------------")


if __name__ == "__main__":
    main()

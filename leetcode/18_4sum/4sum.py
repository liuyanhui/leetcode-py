"""
https://leetcode.com/problems/4sum/
18. 4Sum
Medium
----------
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.
Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
import collections


class Solution:
    def fourSum(self, nums, target):
        return self.fourSum_1(nums, target)

    def fourSum_1(self, nums, target):
        """
        参考思路:
        https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)
        https://leetcode.com/problems/4sum/discuss/8547/7ms-java-code-win-over-100
        思路解析:
        使用递归方法,把4sum转为3sum,进而再转化为2sum.
        时间复杂度为O(N**3)
        ------------
        验证通过
        Runtime: 396 ms, faster than 57.52% of Python3 online submissions for 4Sum.
        Memory Usage: 14 MB, less than 34.47% of Python3 online submissions for 4Sum.
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        ret = []

        def findNsum(n, t, N, beg, t_cache):
            """
            :param n: nums全集
            :param t: 当前的target值
            :param N: N_sum
            :param beg: nums中的开始index
            :param t_cache: 已经计算过的nums元素
            :return:
            """
            if len(n) < N or N < 2 or t < n[0] * N or t > n[-1] * N:  # early termination
                return
            if N == 2:
                # N=2时,转化为2_sum问题
                # 用户hashtable的思路,不适用于此类问题,因为nums中存在重复的数字.使用hashtable需要记录每个数字出现的次数,在计算过程中还需要对次数进行增减,很繁琐.
                # 使用左右夹逼法更合理些.因为nums已经经过排序了
                l, r = beg, len(n) - 1
                while l < r:
                    if n[l] + n[r] == t:
                        t_ret = t_cache + [n[l], n[r]]
                        if t_ret not in ret:
                            ret.append(t_ret)
                        # 去重
                        while l < r and n[l] == n[l + 1]:
                            l += 1
                        while l < r and n[r] == n[r - 1]:
                            r -= 1
                        l, r = l + 1, r - 1
                    elif n[l] + n[r] > t:
                        r -= 1
                    elif n[l] + n[r] < t:
                        l += 1

                return

            for i in range(beg, len(n)):
                t_cache.append(n[i])
                findNsum(n, t - n[i], N - 1, i + 1, t_cache)
                t_cache.pop()
                # 上面的这三行代码可以有下面的这一行代码替换
                # findNsum(n,t-n[i], N - 1, i + 1, t_cache+[n[i]])

        cache = []
        findNsum(nums, target, 4, 0, cache)
        return ret

    def fourSum_recursive(self, nums, target):
        """
        暴力+递归思路
        Time Complexity:O(N**4)
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return []
        ret = set()
        nums.sort()

        def do_recursive(n, t, exist, index):
            if len(exist) == 4:
                if sum(exist) == target:
                    ret.add(tuple(exist))
                return
            for i in range(index, len(nums)):
                exist.append(nums[i])
                do_recursive(n, t, exist, i + 1)
                exist.pop()

        cache = []
        do_recursive(nums, target, cache, 0)
        return [list(r) for r in ret]


def main():
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    ret = Solution().fourSum(nums, target)
    print(ret)
    print(ret == [
        [-1, 0, 0, 1],
        [-2, -1, 1, 2],
        [-2, 0, 0, 2]
    ])
    print('--------------------')

    nums = [-1, 0, -5, -2, -2, -4, 0, 1, -2]
    target = -9
    ret = Solution().fourSum(nums, target)
    print(ret)
    print(ret == [[-5, -4, -1, 1], [-5, -4, 0, 0], [-5, -2, -2, 0], [-4, -2, -2, -1]])
    print('--------------------')

    nums = [1]
    target = 0
    ret = Solution().fourSum(nums, target)
    print(ret)
    print(ret == [])
    print('--------------------')

    nums = [1]
    target = 1
    ret = Solution().fourSum(nums, target)
    print(ret)
    print(ret == [])
    print('--------------------')

    nums = [0, 0, 0, 0, 0, 0, 0]
    target = 0
    ret = Solution().fourSum(nums, target)
    print(ret)
    print(ret == [[0, 0, 0, 0]])


if __name__ == "__main__":
    main()

class Solution:
    """
    https://leetcode.com/problems/permutations-ii/
    47. Permutations II
    Medium
    ------------------------------------
    Given a collection of numbers that might contain duplicates, return all possible unique permutations.
    Example:
            Input: [1,1,2]
            Output:
            [
              [1,1,2],
              [1,2,1],
              [2,1,1]
            ]
    """

    def permuteUnique(self, nums):
        if nums is None or len(nums) == 0:
            return []
        ret = []
        # self.real_permuteUnique_1(nums, 0, ret)
        dict_ret = {}
        self.real_permuteUnique_2(nums, 0, dict_ret)
        ret = list(dict_ret.values())
        return ret

    def real_permuteUnique_1(self, nums, beg, ret):
        """
        思路:
        先求出permutation,再去重
        结果:
        Time Limit Exceeded,执行时间超时
        :param nums:
        :param beg:
        :param ret:
        :return:
        """

        if beg == len(nums):
            tmp = str(nums)
            for r in ret:
                if str(r) == tmp:
                    return
            ret.append(nums.copy())
            return
        for i in range(beg, len(nums)):
            self.swap(nums, beg, i)
            self.real_permuteUnique_1(nums, beg + 1, ret)
            self.swap(nums, i, beg)

    def real_permuteUnique_2(self, nums, beg, dict_ret):
        """
        real_permuteUnique_1的优化版本,缩短了耗时
        :param nums:
        :param beg:
        :param ret:
        :return:
        """

        if beg == len(nums):
            dict_ret[str(nums)]=nums.copy()
            return
        for i in range(beg, len(nums)):
            self.swap(nums, beg, i)
            self.real_permuteUnique_2(nums, beg + 1, dict_ret)
            self.swap(nums, i, beg)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


def main():
    a = [1, 1, 2]
    ret = Solution().permuteUnique(a)
    print(ret)
    print("-------------")

    a = [-1, 2, -1, 2, 1, -1, 2, 1]
    ret = Solution().permuteUnique(a)
    print(ret)
    print("-------------")


if __name__ == '__main__':
    main()

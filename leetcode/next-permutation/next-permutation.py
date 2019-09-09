class Solution:
    """
    https://leetcode.com/problems/next-permutation/
    31. Next Permutation
    Medium
    --------------
    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
    If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
    The replacement must be in-place and use only constant extra memory.
    Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
    """

    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        self.nextPermutation_3(nums)

    def nextPermutation_1(self, nums):
        """
        根据分析:
        1.如果把nums通过递增或递减进行分段,结果是最后一个单调递增分段的最后两位互换.
        2.如果整个nums是递减的,结果是最小值,即反转nums
        结果:
        nums=[1, 3, 2]验证失败
        Output = [3,1,2]
        Expected=[2,1,3]
        :param nums:
        :return:
        """
        last_asc_idx = 0
        asc = False
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                last_asc_idx = i
                asc = True
        if not asc:
            self.swap(nums, 0, len(nums) - 1)
        else:
            self.swap(nums, last_asc_idx, last_asc_idx - 1)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def nextPermutation_2(self, nums):
        """
        采用Permutation思路
        1.先求出所有的Permutation序列
        2.排序
        3.找到所求
        结果:
        Time Limit Exceeded
        :param nums:
        :return:
        """
        ret = []
        self.hepler(nums, 0, ret)
        # print(ret)
        ret.sort()
        for i in range(len(ret)):
            if ret[i] == nums:
                if i < len(ret) - 1:
                    # 跳过重复的排列
                    if ret[i] == ret[i + 1]:
                        continue
                    self.in_replace(nums, ret[i + 1])
                elif i == len(ret) - 1:
                    self.in_replace(nums, ret[0])
                break

    def hepler(self, nums, beg, ret):
        if beg == len(nums):
            ret.append(nums.copy())
            return

        for i in range(beg, len(nums)):
            self.swap(nums, i, beg)
            self.hepler(nums, beg + 1, ret)
            self.swap(nums, beg, i)

    def in_replace(self, src, dest):
        for i in range(len(src)):
            src[i] = dest[i]

    def nextPermutation_3(self, nums):
        """
        参考思路1:
        https://leetcode.com/problems/next-permutation/discuss/13867/C%2B%2B-from-Wikipedia
        According to Wikipedia(https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order), a man named Narayana Pandita presented the following simple algorithm to solve this problem in the 14th century.
        Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
        Find the largest index l > k such that nums[k] < nums[l].
        Swap nums[k] and nums[l].
        Reverse the sub-array nums[k + 1:].
        参考思路2:
        https://leetcode.com/problems/next-permutation/solution/

        :param nums:
        :return:
        """
        if nums is None or len(nums) <= 1:
            return

        s1, s2 = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i - 1] < nums[i]:
                s1 = i - 1
                break
            if i - 1 == 0:
                nums.reverse()
                return

        for i in range(len(nums) - 1, -1, -1):
            if nums[s1] < nums[i]:
                self.swap(nums, s1, i)
                break

        i, j = s1 + 1, len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1


def main():
    a = [1, 2, 3]
    Solution().nextPermutation(a)
    print(a)
    print("------------")

    a = [1, 3, 2]
    Solution().nextPermutation(a)
    print(a)
    print("------------")

    a = [3, 2, 1]
    Solution().nextPermutation(a)
    print(a)
    print("------------")

    a = [1, 1, 5]
    Solution().nextPermutation(a)
    print(a)
    print("------------")

    a = [1, 1, 5, 5]
    Solution().nextPermutation(a)
    print(a)
    print("------------")

    a = [3, 2, 4, 1]
    Solution().nextPermutation(a)
    print(a)
    print("------------")

    a = [3, 1, 4, 4, 2, 3, 4, 0, 0]
    Solution().nextPermutation(a)
    print(a)
    print("------------")


if __name__ == "__main__":
    main()

"""
60. Permutation Sequence
Hard
----------------------------
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"

Example 3:
Input: n = 3, k = 1
Output: "123"

Constraints:
1 <= n <= 9
1 <= k <= n!
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return self.getPermutation_1(n, k)

    def getPermutation_1(self, n: int, k: int) -> str:
        """
        Round 3
        Score[1] Lower is harder

        Thinking：
        1. 递归穷举法（会超时） or 公式计算法
        2. 公式计算法。
        2.1. 因为结果隐含要求从小到大，所以优先选择最小的数字。
        nums：正向排序的待选择的数字集合
        k：结果的序号
        facts：数字对应的阶乘的结果数量
        While k>0
            l = len(nums)
            t = k/facts[l-1]
            ret.append(nums[t])
            k = k%facts[l-1]
            nums.remove(t)

        参考文档:
        https://leetcode.com/problems/permutation-sequence/solutions/22507/explain-like-i-m-five-java-solution-in-o-n/

        验证通过:
        Runtime 41 ms Beats 52.40%
        Memory 17.26 MB Beats 44.12%

        Args:
            n:
            k:

        Returns:

        """
        ret = ''
        nums = [i + 1 for i in range(n)]
        facts = [i for i in range(n + 1)]
        facts[0] = 1
        for i in range(1, n + 1):
            facts[i] = facts[i - 1] * i
        k -= 1  # review 这里很关键.使用除法分割数时,需要考虑边界.如:t=m//6时,需要注意m=6时,应该落在哪里.
        for i in range(n):
            t = k // facts[len(nums) - 1]  # 根据n-1时阶乘划分
            ret += str(nums[t])  # 先提取第一个数字
            k %= facts[len(nums) - 1]  # 更新k,去掉已经计算的部分
            nums.remove(nums[t])  # 移除已经计算过的数字

        return ret


def do_func(n: int, k: int, expect: str):
    ret = Solution().getPermutation(n, k)
    print(ret)
    print(ret == expect)
    print("---------------------")


def main():
    do_func(3, 3, "213")
    do_func(3, 6, "321")
    do_func(4, 9, "2314")
    do_func(3, 1, "123")
    do_func(9, 1000, "124658793")
    do_func(1, 1, "1")


if __name__ == "__main__":
    main()

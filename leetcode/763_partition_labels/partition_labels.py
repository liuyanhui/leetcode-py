"""
https://leetcode.com/problems/partition-labels/
763. Partition Labels
Medium
----------------------
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:
S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""


class Solution:
    def partitionLabels(self, S):
        return self.partitionLabels_2(S)

    def partitionLabels_1(self, S):
        """
        思路:公有两种类型的操作:遍历和合并
        1.遍历字符字符串,保存在数组T[]中,每个元素作为一个单独的数组
        2.如果S[i]出现在T[j0]~T[j1]中,合并T[j0]~T[j1]和S[i],作为T[]的最后一个元素;
        3.否则,S[i]加入T[]中,作为最后一个元素
        4.重复步骤2,3
        5.计算T[]中每个子数组的长度,记为所求
        时间复杂度O(n*n)
        ---------------
        验证通过,性能一般,内存使用量还可以:
        Runtime: 64 ms, faster than 13.34% of Python3 online submissions for Partition Labels.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Partition Labels.
        :param S:
        :return:
        """
        if not S:
            return []
        partition_list = []
        for s in S:
            partition_list.append(s)
            for i in range(len(partition_list) - 1):  # 跳过最后一个元素,因为它刚加入,属于未判断的待定状态
                if s in partition_list[i]:
                    partition_list[i] = "".join(partition_list[i:])
                    partition_list[i + 1:] = []
                    break
        print(partition_list)
        return [len(arr) for arr in partition_list]

    def partitionLabels_2(self, S):
        """
        更优的办法,参考思路:https://leetcode.com/articles/partition-labels/
        属于two-pointers类题目
        1.如何定位每个partition最后一个字符是关键,即partition的最大边界j是关键.j的计算规律是关键.
        2.由于字符的交叉出现,partition的最大边界j,在求解过程中的变化的.
        :param S:
        :return:
        """
        last = {c: i for i, c in enumerate(S)}
        ret = []
        j, anchor = 0, 0
        for i, c in enumerate(S):
            j = max(j, last[c])  # 关键步骤,注意j是动态变化的
            if i == j:  # 匹配到partition
                ret.append(i - anchor + 1)
                anchor = i + 1
        return ret


def main():
    s = "ababcbacadefegdehijhklij"
    ret = Solution().partitionLabels(s)
    print(ret)
    print("--------------------")

    s = "ababcbacadefegdebhijhklij"
    ret = Solution().partitionLabels(s)
    print(ret)
    print("--------------------")

    s = "ababcbacadefegdeahijhklijb"
    ret = Solution().partitionLabels(s)
    print(ret)
    print("--------------------")

    s = "aaaaaaaaaa"
    ret = Solution().partitionLabels(s)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()

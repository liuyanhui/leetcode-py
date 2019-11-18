"""
https://leetcode.com/problems/group-anagrams/
49. Group Anagrams
Medium
----------------
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""
import collections


class Solution:
    def groupAnagrams(self, strs):
        return self.groupAnagrams_2(strs)

    def groupAnagrams_1(self, strs):
        """
        1.计算每个字符串s的特征值,记为T.特征值采用字母排序后的字符串表示
        2.执行ret[T].append(s)
        时间复杂度:O(N*K*logK),N是字符串数量,K是字符串中最大字母个数
        空间复杂度:O(N*K)
        ---------------
        验证通过,性能不错:
        Runtime: 92 ms, faster than 99.46% of Python3 online submissions for Group Anagrams.
        Memory Usage: 15.6 MB, less than 96.23% of Python3 online submissions for Group Anagrams.
        :param strs:
        :return:
        """
        if not strs:
            return []
        ret = collections.defaultdict(list)

        for s in strs:
            ret[''.join(sorted(s))].append(s)
        return [v for v in ret.values()]

    def groupAnagrams_2(self, strs):
        """
        特征值的计算方式与groupAnagrams_1()不同,采用每个字母出现的次数的数字形式,每个特征值的长度都是26
        时间复杂度:O(N*K)
        空间复杂度:O(N*K)
        :param strs:
        :return:
        """
        if not strs:
            return []

        ret = collections.defaultdict(list)
        for s in strs:
            feature = [0] * 26
            for i in s:
                feature[ord(i) - ord('a')] += 1
            ret[tuple(feature)].append(s)
        return [v for v in ret.values()]


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    ret = Solution().groupAnagrams(strs)
    print(ret)
    print("--------------------")

    strs = ["sss", "sss"]
    ret = Solution().groupAnagrams(strs)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()

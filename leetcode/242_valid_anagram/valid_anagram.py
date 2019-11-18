"""
https://leetcode.com/problems/valid-anagram/
242. Valid Anagram
Easy
---------------------
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
import collections


class Solution:
    def isAnagram(self, s, t):
        return self.isAnagram_2(s, t)

    def isAnagram_1(self, s, t):
        """
        验证通过
        时间复杂度:O(N*logN)
        空间复杂度:O(N)
        :param s:
        :param t:
        :return:
        """
        if not s or not t:
            return True
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def isAnagram_2(self, s, t):
        """
        验证通过
        时间复杂度:O(N)
        空间复杂度:O(N)
        :param s:
        :param t:
        :return:
        """
        if not s or not t:
            return True
        if len(s) != len(t):
            return False
        s_dict, t_dict = collections.defaultdict(int), collections.defaultdict(int)
        for i in range(len(s)):
            s_dict[ord(s[i]) - ord('a')] += 1
            t_dict[ord(t[i]) - ord('a')] += 1
        for i in s_dict.keys():
            if s_dict[i] != t_dict[i]:
                return False
        return True


def main():
    s = "anagram"
    t = "nagaram"
    ret = Solution().isAnagram(s, t)
    print(ret)
    print("--------------------")

    s = "rat"
    t = "car"
    ret = Solution().isAnagram(s, t)
    print(ret)
    print("--------------------")


if __name__ == "__main__":
    main()
